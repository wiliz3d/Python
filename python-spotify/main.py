import tkinter as tk
from tkinter import filedialog
import pygame
import spotipy
import spotipy.util as util
from spotipy import SpotifyOAuth
from spotify import oauth
import customtkinter
from tkinter import messagebox as Mb
from spotipy.oauth2 import SpotifyClientCredentials
import requests


customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')


class App(customtkinter.CTk):
    def __init__(self):
         super().__init__()
         self.geometry("300x500")
         self.title('Player-Gui')
         self.resizable(False, False)
         
         self.mainframe = customtkinter.CTkFrame(self,width=290,height=490)
         self.mainframe.pack(padx=0,pady=0)
          # Create a label for displaying the song name
          
         self.song_label = customtkinter.CTkLabel(self.mainframe, text="No song selected",
                                                  text_color='White',font=('San Francisco', 25,'bold'),
                                                  corner_radius=30,width=30)
         self.song_label.place(relx=0.03,rely=0.04)
         
          # Create a button for selecting a song
         self.select_button = customtkinter.CTkButton(self.mainframe, text="Select Song",
                                                      text_color='White',
                                                      width=30,font=('San Francisco', 20,'bold'),
                                                      corner_radius=6,
                                                      command=self.select_song)
         self.select_button.place(relx=0.03,rely=0.2)

        # Create a button for playing and pausing the selected song
         self.play_button = customtkinter.CTkButton(self.mainframe, text="Play", 
                                                    text_color='White',font=('San Francisco', 20,'bold'),
                                                    width=30,corner_radius=6
                                                    ,command=self.play_pause)
         self.play_button.place(relx=0.03,rely=0.4)

        # Create a variable for tracking whether the song is playing or paused
         self.playing = False
         
    def select_song(self, track_id):
        # Spotify API and client credentials
        client_id = '2e6feb40ec9c429eab6bacfaa825549d'
        client_secret = '7deffc4325204574bd03f497398e434a'
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        spoti = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        
        # Use the Spotify API to get the track information
        track = spoti.track(track_id)
            
        # Get the preview URL for the track
        preview_url = track["preview_url"]
        
        # Download the audio file from the preview URL
        response = requests.get(preview_url)
        
        # Save the audio file to disk
        with open("audio.mp3", "wb") as f:
            f.write(response.content)
            
        # Load the audio file into Pygame
        pygame.mixer.music.load("audio.mp3")
        
        # Update the song label
        song_name = track["name"]
        self.song_label.config(text=song_name)
        
    def play_pause(self):
        if self.playing:
            # If the song is currently playing, pause it and update the button text
            pygame.mixer.music.pause()
            self.play_button.config(text="Play")
            self.playing = False
        else:
            # If the song is currently paused, play it and update the button text
            pygame.mixer.music.unpause()
            self.play_button.config(text="Pause")
            self.playing = True

        
player_gui = App()