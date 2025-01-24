from analyze_playlist import combine_playlists, analyze_playlists
from get_playlist import fetch_playlist_data,save_to_folder
from search_spotify import search_playlists
import numpy
import tkinter 
from tkinter import *


def big_function(): 
    query=entry1.get()
    limit=int(entry2.get())
    playlist_urls=search_playlists(query, limit)
    for x in numpy.arange(limit):
        data=fetch_playlist_data(playlist_urls[x])
        save_to_folder(data, "csv_files", str(x)+".csv")
    combined_playlist=combine_playlists(limit)
    analyzed_playlist=analyze_playlists(combined_playlist,10)
    result = analyzed_playlist
    text1.delete(1.0, tkinter.END) 
    text1.insert(tkinter.END, result) 


popup=tkinter.Tk()
popup.title("Shitty program I made")
popup.geometry("700x550")
label1 = tkinter.Label(popup, text="This is a tool that works with playlists", font=("Times New Roman", 18))
label1.pack(pady=10)
label2 = tkinter.Label(popup, text="It searches Spotify for playlists and shows which songs are most common", font=("Times New Roman", 16))
label2.pack(pady=10)
label3 = tkinter.Label(popup, text="Query", font=("Times New Roman", 12))
label3.pack(pady=5)
entry1 = tkinter.Entry(popup)
entry1.pack(pady=5)
label4 = tkinter.Label(popup, text="Number of playlists to search", font=("Times New Roman", 12))
label4.pack(pady=5)
entry2 = tkinter.Entry(popup)
entry2.pack(pady=5)
search_button = tkinter.Button(popup, text="Search", font=("Times New Roman", 12), command=big_function)
search_button.pack(pady=25)
label5 = tkinter.Label(popup, text="Results", font = ("Times New Roman", 18))
label5.pack(pady=5)
text1= tkinter.Text(popup, wrap="word", height=10, width=50)
text1.pack(pady=10)
popup.mainloop()

'''
print("Hello! I make playlists based on Spotify data")
query=input("Give me a word or phrase, and I'll gather the top X playlists on Spotify with that word or phrase in the name")
limit=int(input("Give me a number under 50 bc this computer sucks to search"))
songs=int(input("Give me another number for the compiled playlist's amount of songs"))
'''

