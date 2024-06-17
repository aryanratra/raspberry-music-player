"""Contains small functions for basic repetitive tasks like import icons, images etc."""
import os
from tkinter import PhotoImage
from config import ICONS_PATH

def load_icon(file_name):
    """Loads icons as a PhotoImage."""
    return PhotoImage(file=os.path.join(ICONS_PATH, file_name))

def load_default_cover(size):
    """Loads default cover art as a PhotoImage."""
    if size == 0:
        return PhotoImage(file=r"./assets/default_cover_44px.png")
    return PhotoImage(file=r"./assets/default_cover.png")
