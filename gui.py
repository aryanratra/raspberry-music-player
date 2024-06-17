import tkinter as tk
from ttkbootstrap.constants import *
from tkinter import Frame, Button, PhotoImage
from config import *


class MusicPlayerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player App")
        self.window.geometry("320x480")
        self.window.configure(background=DARK_BG)

    def run(self):
        self.window.mainloop()