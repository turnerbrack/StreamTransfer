from django.contrib import admin
from django.urls import path
from StreamTransferApp.views import playlists, transfer_playlists, home, login_tidal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/tidal/', login_tidal),
    path('playlists/', playlists),
    path('playlists/transfer/', transfer_playlists),
]