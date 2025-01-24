import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "1aa048b442f74df1b692599763a70173"
CLIENT_SECRET = "a321f91c17814925b385e936fd2786ef"
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def search_playlists(query, limit=50):
    playlist_urls = []
    result = sp.search(q=query, type='playlist', limit=limit)
    # Add the playlists from the first page
    playlist_urls.extend(playlist['external_urls']['spotify'] for playlist in result['playlists']['items'] if playlist)
    
    # Check if more playlists are available via pagination
    while result['playlists']['next'] and len(playlist_urls) < limit:
        result = sp.next(result['playlists'])
        
        # Add playlists from the next pages until we reach the limit
        playlist_urls.extend(playlist['external_urls']['spotify'] for playlist in result['playlists']['items'] if playlist)
        
        # Stop if we've reached the desired limit
        if len(playlist_urls) >= limit:
            break
         
    return playlist_urls[:limit]  # Ensure that we only return the first 'limit' playlists

