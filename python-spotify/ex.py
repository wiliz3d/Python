import customtkinter
from tkinter import *
import pygame
import spotify
from spotify import SpotifyBase
import os
from tkinter import messagebox



customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('blue')


class App(customtkinter.CTk):
    def __init__(self):
         super().__init__()
         self.geometry("400x500")
         self.title('Music Player')
         self.resizable(False, False)
         pygame.mixer.init()
         
         
         self.mainframe = customtkinter.CTkFrame(self,width=390,height=490)
         self.mainframe.pack(padx=0,pady=0)
          # Create a label for displaying the song name
          
         self.song_label = customtkinter.CTkLabel(self.mainframe, text="No song selected",
                                                  text_color='White',font=('San Francisco', 25,'bold'),
                                                  corner_radius=30,width=30)
         self.song_label.place(relx=0.03,rely=0.04)
         
         self.list = customtkinter.CTkScrollableFrame(self.mainframe,width=350,height=35)
         self.list.place(relx=0.03, rely=0.12)
         
         self.play_btn = PhotoImage(file='play.png')
         self.pause_btn = PhotoImage(file='pause.png')
         self.next_btn = PhotoImage(file='next.png')
         self.rev_btn = PhotoImage(file='previous.png')
         
         self.control_frame = customtkinter.CTkFrame(self.mainframe)
         self.control_frame.place(relx=0.03,rely=0.25)
         
         playbtn = Button(self.control_frame, image=self.play_btn, border_width=0)
         pausebtn = Button(self.control_frame, image=self.pause_btn, border_width=0)
         nextbtn = Button(self.control_frame, image=self.next_btn, border_width=0)
         revbtn = Button(self.control_frame, image=self.rev_btn, border_width=0)
         
         playbtn.grid(row=0,coloumn=0,padx=7,pady=10)
         pausebtn.grid(row=0,coloumn=1,padx=7,pady=10)
         nextbtn.grid(row=0,coloumn=2,padx=7,pady=10)
         revbtn.grid(row=0,coloumn=3,padx=7,pady=10)
         
                             
if __name__ == '__main__':
    app = App()
    app.mainloop()