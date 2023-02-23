import tkinter as tk
import spotipy
import spotipy.util as util
import pygame

class SpotifyPlayer(tk.Tk):
    def __init__(self, client_id, client_secret, redirect_uri, username):
        super().__init__()

        # Set up the Spotify API credentials
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.username = username

        # Set up the Spotipy library with your API credentials
        self.scope = 'user-read-private user-read-playback-state user-modify-playback-state'
        self.token = util.prompt_for_user_token(self.username, self.scope, client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri)
        self.sp = spotipy.Spotify(auth=self.token)

        # Set up the Pygame library for playing audio
        pygame.init()
        pygame.mixer.init()

        # Create the main window and frame
        self.title('Spotify Player')
        self.frame = tk.Frame(self)
        self.frame.pack()

        # Create the track entry and search button
        self.track_entry = tk.Entry(self.frame)
        self.track_entry.pack(side=tk.LEFT)
        self.search_button = tk.Button(self.frame, text='Search', command=lambda: self.play_track(self.track_entry.get()))
        self.search_button.pack(side=tk.LEFT)

        # Create the track label, artist label, album label, and cover label
        self.track_label = tk.Label(self, text='Track Name', font=('Arial', 18))
        self.track_label.pack()
        self.artist_label = tk.Label(self, text='Artist Name', font=('Arial', 14))
        self.artist_label.pack()
        self.album_label = tk.Label(self, text='Album Name', font=('Arial', 12))
        self.album_label.pack()
        self.cover_label = tk.Label(self)

    def play_track(self, track_name):
        result = self.sp.search(q='track:' + track_name, type='track', limit=1)
        if result['tracks']['total'] > 0:
            track = result['tracks']['items'][0]
            track_uri = track['uri']
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            album_name = track['album']['name']
            #cover_url = track['album']['images'][0]['url']
            cover_data = self.sp._get(cover_url)['content']
            cover_file = open('cover.jpg', 'wb')
            cover_file.write(cover_data)
            cover_file.close()
            pygame.mixer.music.load(track_uri)
            pygame.mixer.music.play()
            self.track_label.config(text=track_name)
            self.artist_label.config(text=artist_name)
            self.album_label.config(text=album_name)
            cover_image = tk.PhotoImage(file='cover.jpg')
            self.cover_label.config(image=cover_image)
            self.cover_label.image = cover_image
            self.cover_label.pack()
        else:
            self.track_label.config(text='Track not found')
            self.artist_label.config(text='')
            self.album_label.config(text='')
            self.cover_label.config(image=None)

if __name__ == '__main__':
    # Set up your Spotify API credentials
    CLIENT_ID = '2e6feb40ec9c429eab6bacfaa825549d'
    CLIENT_SECRET = '7deffc4325204574bd03f497398e434a'
    REDIRECT_URI = 'http://localhost:8888/callback'
    USERNAME = 'your_spotify_username'

    # Create a new SpotifyPlayer object 
    player = SpotifyPlayer
