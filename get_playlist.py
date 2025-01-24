import csv
import pandas
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
import os

CLIENT_ID = "1aa048b442f74df1b692599763a70173" 
CLIENT_SECRET = "a321f91c17814925b385e936fd2786ef"  
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = Spotify(client_credentials_manager=client_credentials_manager)

def fetch_playlist_data(playlist_url):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    track_data = []
    for item in tracks:
        track = item.get('track')
        if not track:
            print("Skipping item without track data:", item)
            continue
        artist_names = [
            artist.get('name', "Unknown") for artist in track.get('artists', [])
            if artist.get('name') is not None
        ]
        spotify_url = track.get('external_urls', {}).get('spotify', "N/A")
        track_data.append({
            "Track Name": track.get('name', "Unknown"),
            "Artist(s)": ", ".join(artist_names) or "Unknown",
            "Album": track.get('album', {}).get('name', "Unknown"),
            "Release Date": track.get('album', {}).get('release_date', "Unknown"),
            "Duration (ms)": track.get('duration_ms', 0),
            "Spotify URL": spotify_url,
        })
    return track_data


def save_to_folder(data, folder_path, file_name):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    keys = data[0].keys()
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"Playlist data saved to {file_name}")
    print(f"Playlist data saved to {file_path}") 
    return file_path

def list_csv_files(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist!")
        return []
    return [file for file in os.listdir(folder_path) if file.endswith('.csv')]