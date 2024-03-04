import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd 
import pandasql as ps
from dotenv import dotenv_values


config = dotenv_values(".env")

client_id = config["SpotyClienteID"]
client_secret = config["SpotyClienteSecret"]

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#https://open.spotify.com/playlist/37i9dQZF1DX5BAPG29mHS8?si=e5cf8c08fb6945ca
#https://open.spotify.com/playlist/37i9dQZF1DX10zKzsJ2jva?si=5136e1a1400f402e
#https://open.spotify.com/playlist/37i9dQZF1DX21ow0o1PZDE?si=a55e3e6171184107

playlists ={
    "37i9dQZF1DX5BAPG29mHS8" : "ExitosMexio",
    "37i9dQZF1DX10zKzsJ2jva" :"VivaLatino",
    "37i9dQZF1DX21ow0o1PZDE" :"Exitos2024"
}

tracks_data = []

# Iteramos sobre cada playlist

# for playlist_id, playlist_name in playlists.items():
#     print(f"Obteniendo informacion de la playlist {playlist_name}")
#     playlist = sp.playlist(playlist_id)
#     tracks = playlist["tracks"]["items"]
    
#     for track in tracks:
#         track_info = track["track"]
#         id_track = track_info["id"]
#         name = track_info["name"]
#         popularity = track_info["popularity"]
#         artist = track_info["artists"][0]["name"]
#         album = track_info["album"]["name"]
#         release_date = track_info["album"]["release_date"]
        
#         tracks_data.append([id_track, name, artist, album, release_date, popularity, playlist_name])
        
for playlist_id, playlist_name in playlists.items():
    results = sp.playlist_tracks(playlist_id)
    for i, item in enumerate(results['items']):
        track = item['track']
        #print(f"  track tiene {i} {track}")
        print(f"{i} {track['name']} {track['id']}")
        track_info = {
            'Posicion': i +1,
            "Nombre de la cancion": track['name'],
            "Artista": ", ".join([artist['name'] for artist in track['artists']]),
            "Popularidad": track['popularity'],
            "Duration_ms": track['duration_ms'],
            "ReleaseDate": track['album']["release_date"]
        }    
        tracks_data.append(track_info)
        
# Crear dataframe  

df_tracks = pd.DataFrame(tracks_data)
df_tracks.to_csv("tracks.csv", index=False)
