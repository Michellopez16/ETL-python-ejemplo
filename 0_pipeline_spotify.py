import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pandas as pd 
from dotenv import dotenv_values


config = dotenv_values(".env")

client_id = config["SpotyClienteID"]
client_secret = config["SpotyClienteSecret"]

client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

nombre_artista = 'Benson Boone'
resultado = sp.search(q='artist: ' + nombre_artista, type='artist')

artistas = resultado['artists']['items']

lista_artistas = []

for artista in artistas:
    nombre = artista['name']
    popularidad = artista['popularity']
    seguidores = artista['followers']['total']
    lista_artistas.append([nombre, popularidad, seguidores])

#Creamos el dataframe

df_artistas = pd.DataFrame(lista_artistas, columns=['nombre', 'popularidad', 'seguidores'])
print(df_artistas)

