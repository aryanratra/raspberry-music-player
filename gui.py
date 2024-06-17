"""Creates and maintains all the GUI of the app."""
import tkinter as tk
from tkinter import Frame, Button, Label
from ttkbootstrap.constants import LEFT, RIGHT, TRUE, FALSE
from config import DARK_BG, DARK_BG_2, TEXT_W
from utils import load_icon, load_default_cover

class MusicPlayerApp:
    """Music Player class for the GUI."""
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player App")
        self.window.geometry("320x480")
        self.window.configure(background=DARK_BG)

        #Creating Frames
        self.file_browser = Frame(master=self.window)
        self.top_bar = Frame(master=self.file_browser)
        self.address_bar = Frame(master=self.file_browser)
        self.file_view = Frame(master=self.file_browser)
        self.music_player = Frame(master=self.window)

        #Icons for buttons
        self.home_btn_img = load_icon("Home_Btn.png")
        self.back_btn_img = load_icon("Back_Btn.png")
        self.cover_art_sml_img = load_default_cover(0)
        self.play_btn_img = load_icon("Play_Btn.png")

        #Creating all labels
        self.app_title_label = Label(master=self.top_bar)
        self.address_label = Label(master=self.address_bar)

        #Creating all button
        self.home_btn = Button(master=self.top_bar)
        self.back_btn = Button(master=self.address_bar)
        self.music_btn = Button(master=self.music_player)
        self.play_btn = Button(master=self.music_player)

        self.setup_ui()

    def setup_ui(self):
        """Setup all UI elements."""
        self.create_components()
        self.create_file_browser()
        self.create_music_player()

    def create_components(self):
        """Create all individual components."""
        #===========COMPACT MUSIC WINDOW===========
        #Configuring all frames
        self.top_bar.configure(padx=15, pady=15,background=DARK_BG)
        self.address_bar.configure(padx=15, pady=8,background=DARK_BG_2)
        self.music_player.configure(padx=15, pady=15,background=DARK_BG_2)

        #Configuring all button
        song_title = "Turn Up The Speakers"
        self.home_btn.configure(image=self.home_btn_img)
        self.home_btn.configure(background=DARK_BG, borderwidth=0, activebackground=DARK_BG)
        self.home_btn.pack(side=RIGHT)
        self.back_btn.configure(image=self.back_btn_img)
        self.back_btn.configure(background=DARK_BG_2, borderwidth=0, activebackground=DARK_BG_2)
        self.back_btn.pack(side=LEFT)
        self.music_btn.configure(text=song_title, font=("Arial", 13, "normal"))
        self.music_btn.configure(image=self.cover_art_sml_img, foreground=TEXT_W)
        self.music_btn.configure(background=DARK_BG_2, borderwidth=0, activebackground=DARK_BG_2)
        self.music_btn.configure(padx=12, compound="left", justify=LEFT)
        self.music_btn.pack(side=LEFT)
        self.play_btn.configure(image=self.play_btn_img)
        self.play_btn.configure(background=DARK_BG_2, borderwidth=0, activebackground=DARK_BG_2)
        self.play_btn.pack(side=RIGHT)

        #Configuring all labels
        self.app_title_label.configure(text="Music Player", font=("Arial", 19, "normal"))
        self.app_title_label.configure(anchor="w", background=DARK_BG, foreground=TEXT_W)
        self.app_title_label.pack(side=LEFT, expand=TRUE, fill="x")

    def create_file_browser(self):
        """Setup and pack the file browser."""
        self.top_bar.pack(expand=TRUE, fill="x")
        self.address_bar.pack(expand=TRUE, fill="x")
        self.file_browser.pack(expand=FALSE, fill="both")

    def create_music_player(self):
        """"Setup and pack the music player."""
        self.music_player.pack(expand=FALSE, side="bottom",fill="x")

    def run(self):
        """Run the main loop event."""
        self.window.mainloop()
