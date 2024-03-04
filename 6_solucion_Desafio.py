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


# Top 50 de diferentes paises

#Mexico #https://open.spotify.com/playlist/37i9dQZEVXbO3qyFxbkOE1?si=c261245c55b941fa 
#Global #https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF?si=a8b927d2ec7944bb
#USA #https://open.spotify.com/playlist/37i9dQZEVXbLRQDuF5jeBp?si=529d329106dd4e9a
#España #https://open.spotify.com/playlist/37i9dQZEVXbNFJfN1Vw8d9?si=f78d8189a7924a41
#Colombia #https://open.spotify.com/playlist/37i9dQZEVXbOa2lmxNORXQ?si=4b6ef9cad4854e1f
#Argentina #https://open.spotify.com/playlist/37i9dQZEVXbMMy2roB9myp?si=40856706aaf842ab

playlists ={
    "37i9dQZEVXbO3qyFxbkOE1" : "Mexico",
    "37i9dQZEVXbMDoHDwVN2tF" : "Global",
    "37i9dQZEVXbLRQDuF5jeBp" : "USA",
    "37i9dQZEVXbNFJfN1Vw8d9" : "España",
    "37i9dQZEVXbOa2lmxNORXQ" : "Colombia",
    "37i9dQZEVXbMMy2roB9myp" : "Argentina",
}

tracks_data = []

# Iteramos sobre cada playlist
        
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
            "ReleaseDate": track['album']["release_date"],
            "Pais": playlist_name
        }    
        tracks_data.append(track_info)
        
# Crear dataframe  

df_tracks = pd.DataFrame(tracks_data)
df_tracks.to_csv("tracks3.csv", index=False)

print(df_tracks)

query = """
SELECT * FROM df_tracks
WHERE Pais IN ('Mexico', 'Global', 'USA', 'España', 'Colombia', 'Argentina')
AND Posicion in (1,2,3,4,5,6,7,8,9,10)
ORDER BY Popularidad DESC
"""

print("-"*40+"Iniciando query"+"-"*40)

top_10_sql = ps.sqldf(query, locals())
nombre_archivo = "top_10_latinoamerica_sql.csv"
top_10_sql.to_csv(nombre_archivo, index = False)
print(f"Se ha guardado el archivo {nombre_archivo}")
print(top_10_sql)
