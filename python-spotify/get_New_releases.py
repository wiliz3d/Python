import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

Client_ID = '2e6feb40ec9c429eab6bacfaa825549d'
Client_Secret = ' 7deffc4325204574bd03f497398e434a'


client_id = Client_ID
client_secret = Client_Secret

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


results = sp.new_releases()
for album in results['albums']['items']:
    print(album['name'])
