import csv
import pandas
import numpy 
import os
from datascience import Table
from datascience import make_array

def combine_playlists(num_playlists):
    folder = 'csv_files'
    songs = Table().with_columns("Track Name", "Artist(s)", "Album", "Release Date", "Duration (ms)", "Spotify URL")
    for i in numpy.arange(num_playlists): 
        path = os.path.join(folder, f"{i}.csv")  # Construct the file path using string formatting
        try:
            df = pandas.read_csv(path)
            ds_table = Table().with_columns(
            *[(col, df[col].values) for col in df.columns]
            )
        except FileNotFoundError:
            print(f"File not found: {path}")
        songs=songs.append(ds_table.exclude(0))
    return songs

def analyze_playlists(Table,x):
    grouped_table=Table.group("Track Name")
    grouped_and_sorted_table=grouped_table.sort('count', descending=True)
    return grouped_and_sorted_table.take(range(x))