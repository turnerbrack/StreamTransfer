from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from StreamTransferApp import apikey
from StreamTransferApp.apikey import get_playlist_art
from django.contrib.auth import decorators as auth_decorators


tidal_session = None
def login_tidal(request):
    global tidal_session
    tidal_session = apikey.authenticate_tidal(request)
    return redirect('/playlists/')

def playlists(request):
    global tidal_session
    tidal_playlists = apikey.get_playlists(tidal_session)
    for playlist in tidal_playlists:
        playlist.art_url = get_playlist_art(tidal_session, playlist)
    request.session.set_expiry(20)  
    return render(request, 'playlists.html', {'playlists': tidal_playlists})

def home(request):
    return render(request, 'home.html')

def transfer_playlists(request):
    if request.method == 'POST':
        tidal_auth = request.session['tidal_auth']
        tidal_playlists = apikey.get_playlists(tidal_auth)

        for tidal_playlist in tidal_playlists:
            tidal_tracks = apikey.get_playlist_tracks(tidal_auth, tidal_playlist)
            spotify_playlist = apikey.create_playlist(spotify_auth, tidal_playlist.name)
            apikey.add_tracks_to_playlist(spotify_auth, spotify_playlist, tidal_tracks)

        return HttpResponse("Playlists transferred successfully!")
    
    return HttpResponse('{"error": "Invalid request method"}')

