import tidalapi
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import urllib.parse



def authenticate_spotify():
    
    client_id = "a7dfb39750d344cca0f3d775e4888147"
    client_secret = "f778902484f4450db4a56bb72ccf6ea8"
    redirect_uri = "https://samplesitebrackturner.com"
    scopes = ["user-library-read playlist-modify-public"]
    
    #authenticate with the Spotify API
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    spotify_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scopes)
    auth_url = spotify_oauth.get_authorize_url()
    print("Open this URL in your browser: ", auth_url)

    auth_code = input("Enter the code from the authorization page: ")
    token_info = spotify_oauth.get_access_token(auth_code)
    access_token = token_info["access_token"]
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    response = sp.me()
    if response:
        print("Your credentials are working!")
    else:
        print("There was an error with your credentials. Please check them and try again.")

    return sp

#authenticate Tidal API
def authenticate_tidal(request):
    session = tidalapi.Session()
    login, future = session.login_oauth()
    auth_url = login.verification_uri_complete
    if not auth_url.startswith("https://"):
        auth_url = "https://" + auth_url
    parsed_url = urllib.parse.urlparse(auth_url)  # Parse the URL
    encoded_query = urllib.parse.quote(parsed_url.query)  # Encode the query string
    auth_url = urllib.parse.urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, parsed_url.params, encoded_query, parsed_url.fragment))  # Rebuild the URL with the encoded query string
    webbrowser.open(auth_url)  # Open the URL in the default web browser
    future.result()  # Block the calling thread until the login process is complete
    
    return session


#get user playlists
def get_playlists(tidal_session):
    print(tidal_session)
    playlists = tidal_session.user.playlists()
    return playlists

def get_playlist_art(tidal_session, tidal_playlist):
    playlist_art = tidal_playlist.image(320)
    return playlist_art

#get user tracks from playlists
def get_playlist_tracks(tidal_session, tidal_playlist):

    tracks = tidal_playlist.tracks(limit=None, offset=0)
    return tracks

def create_playlist(spotify_session, tidal_playlist_name):

    playlist = spotify_session.user_playlist_create(spotify_session.me()['id'], tidal_playlist_name)
    return playlist

def add_tracks_to_playlist(spotify_session, spotify_playlist, tidal_tracks):

    spotify_tracks = []
    for tidal_track in tidal_tracks:
        query = "{} {}".format(tidal_track.artist.name, tidal_track.name)
        results = spotify_session.search(query, type="track")
        spotify_track = results["tracks"]["items"][0]
        spotify_tracks.append(spotify_track['id'])

    spotify_session.user_playlist_add_tracks(spotify_session.me()['id'], spotify_playlist['id'], spotify_tracks)






