import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# set up Spotify API credentials
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# search for an artist by name
artist_name = "Michael-Jackson"
results = sp.search(q=artist_name, type="artist", limit=1)

# get the artist ID from the search results
if len(results["artists"]["items"]) > 0:
    artist_id = results["artists"]["items"][0]["id"]
    print(f"Artist ID for '{artist_name}': {artist_id}")
else:
    print(f"No artist found for '{artist_name}'")
