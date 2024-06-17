"""Creates and maintains all the GUI of the app."""
import os
import tkinter as tk
from tkinter import Frame, Button, Label, Listbox
from ttkbootstrap.constants import LEFT, RIGHT, TRUE, FALSE, END
from config import DARK_BG, DARK_BG_2, TEXT_W, TEXT_G
from utils import load_icon, load_default_cover, list_items

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

        #Create file listbox
        self.file_listbox = Listbox(master=self.file_view)

        #Creating general variables
        self.home_directory = "D:\\Music"
        self.current_directory = ""

        self.setup_ui()

    def setup_ui(self):
        """Setup all UI elements."""
        self.create_components()
        self.create_file_browser()
        self.create_music_player()
        self.update_file_components("D:\\Music")

    def create_components(self):
        """Create all individual components."""
        #===========COMPACT MUSIC WINDOW===========
        #Configuring all frames
        self.top_bar.configure(padx=15, pady=15,background=DARK_BG)
        self.address_bar.configure(padx=15, pady=8,background=DARK_BG_2)
        self.file_view.configure(padx=15, pady=15,background=DARK_BG)
        self.file_browser.configure(padx=0,pady=0, background=DARK_BG)
        self.music_player.configure(padx=15, pady=15,background=DARK_BG_2)

        #Configuring all button
        song_title = "  No Song Playing"
        self.home_btn.configure(image=self.home_btn_img)
        self.home_btn.configure(background=DARK_BG, borderwidth=0, activebackground=DARK_BG)
        self.home_btn.configure(command=lambda: self.update_file_components(self.home_directory))
        self.home_btn.pack(side=RIGHT)

        self.back_btn.configure(image=self.back_btn_img)
        self.back_btn.configure(background=DARK_BG_2, borderwidth=0, activebackground=DARK_BG_2)
        self.back_btn.configure(command=self.back_directory)
        self.back_btn.pack(side=LEFT)

        self.music_btn.configure(text=song_title, font=("Arial", 13, "normal"))
        self.music_btn.configure(image=self.cover_art_sml_img, foreground=TEXT_W)
        self.music_btn.configure(background=DARK_BG_2, borderwidth=0, activebackground=DARK_BG_2)
        self.music_btn.configure(compound="left", justify=LEFT)
        self.music_btn.pack(side=LEFT)

        self.play_btn.configure(image=self.play_btn_img)
        self.play_btn.configure(background=DARK_BG_2, borderwidth=0, activebackground=DARK_BG_2)
        self.play_btn.pack(side=RIGHT)

        #Configuring all labels
        self.app_title_label.configure(text="Music Player", font=("Arial", 19, "normal"))
        self.app_title_label.configure(anchor="w", background=DARK_BG, foreground=TEXT_W)
        self.app_title_label.pack(side=LEFT, expand=TRUE, fill="x")

        self.address_label.configure(text=self.current_directory, font=("Arial", 12, "normal"))
        self.address_label.configure(background=DARK_BG_2, foreground=TEXT_G, justify="center")
        self.address_label.pack(side=RIGHT, expand=True, fill="x")

        #Configuring file listbox
        self.file_listbox.configure(font=("Arial", 12, "normal"), justify="left")
        self.file_listbox.configure(background=DARK_BG, foreground=TEXT_W)
        self.file_listbox.configure(borderwidth=0, highlightthickness=0)
        self.file_listbox.configure(activestyle="none")
        self.file_listbox.pack(side="top",expand=TRUE, fill="both")

    def create_file_browser(self):
        """Setup and pack the file browser."""
        self.top_bar.pack(side="top", expand=FALSE, fill="x")
        self.address_bar.pack(side="top", expand=FALSE, fill="x")
        self.file_view.pack(side="bottom", expand=TRUE, fill="both")
        self.file_browser.pack(expand=TRUE, fill="both")

    def create_music_player(self):
        """"Setup and pack the music player."""
        self.music_player.pack(expand=FALSE, side="bottom",fill="x")

    def update_file_components(self, directory_path):
        """Adds list items (files/folders) to the file view component."""
        directory_path += "\\"
        self.current_directory = directory_path
        self.address_label.configure(text=self.current_directory)
        all_items = list_items(self.current_directory)
        self.file_listbox.delete(0, END)
        for item in all_items:
            if item[1] == "Folder":
                self.file_listbox.insert(END, f"Folder: {item[0]}")
            if item[1] == "File":
                self.file_listbox.insert(END, f"File: {item[0]}")

    def click_list_item(self, event):
        """Clicking items of listbox updates the contents and changes directory."""
        selected_item = self.file_listbox.get(self.file_listbox.curselection())
        file_type, file_name = selected_item.split(":")

        if file_type.strip() == "Folder":
            self.update_file_components(os.path.join(self.current_directory, file_name.strip()))
        elif file_type.strip() == "File":
            print("Song played")

    def back_directory(self):
        """"Functionality for back button to come back to previous directory."""
        if self.current_directory == "D:\\Music\\":
            pass
        else:
            back_directory_path = self.current_directory.rsplit("\\", 2)[0]
            self.update_file_components(back_directory_path)

    def run(self):
        """Run the main loop event."""
        self.file_listbox.bind("<<ListboxSelect>>", self.click_list_item)
        self.window.mainloop()
