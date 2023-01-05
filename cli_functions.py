import requests
import json

base_albums_url = "https://jsonplaceholder.typicode.com/photos"


def get_album_data(album_selection):

    if "-" in album_selection:
        range_start, range_end = album_selection.split("-")
        album_stream = requests.get(f"{base_albums_url}?albumId_gte={range_start}&albumId_lte={range_end}")

    else:
        album_stream = requests.get(f"{base_albums_url}?albumId={album_selection}")

    if album_stream.status_code == 200:
        album_data = album_stream.json()
        return album_stream.json()
    else:
        return None





