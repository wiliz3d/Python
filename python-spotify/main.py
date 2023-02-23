import tkinter as tk
from tkinter import filedialog
import pygame

class PlayerGUI:
    def __init__(self):
        # Set up Pygame for audio playback
        pygame.init()
        pygame.mixer.init()

        # Set up GUI window
        self.window = tk.Tk()
        self.window.title("Music Player")
        
        # Create a label for displaying the song name
        self.song_label = tk.Label(self.window, text="No song selected")
        self.song_label.pack()

        # Create a button for selecting a song
        self.select_button = tk.Button(self.window, text="Select Song", command=self.select_song)
        self.select_button.pack()

        # Create a button for playing and pausing the selected song
        self.play_button = tk.Button(self.window, text="Play", command=self.play_pause)
        self.play_button.pack()

        # Create a variable for tracking whether the song is playing or paused
        self.playing = False

        # Start the GUI main loop
        self.window.mainloop()

    def select_song(self):
        # Open a file dialog to select a song
        file_path = filedialog.askopenfilename()

        # Load the song into Pygame
        pygame.mixer.music.load(file_path)

        # Update the song label
        song_name = file_path.split("/")[-1]
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

# Create the player GUI
player_gui = PlayerGUI()
