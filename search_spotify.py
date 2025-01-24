import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "Get your own Spotify credentials lol"
CLIENT_SECRET = "A secret or sumn"
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_playlists(query, limit=50):
    playlist_urls = []
    result = sp.search(q=query, type='playlist', limit=limit)
    playlist_urls.extend(playlist['external_urls']['spotify'] for playlist in result['playlists']['items'] if playlist)
    while result['playlists']['next'] and len(playlist_urls) < limit:
        result = sp.next(result['playlists'])
        playlist_urls.extend(playlist['external_urls']['spotify'] for playlist in result['playlists']['items'] if playlist)
        if len(playlist_urls) >= limit:
            break
         
    return playlist_urls[:limit]  

