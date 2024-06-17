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


def list_items(directory_address):
    """Returns a list containing all the folders and audio files in a base directory."""
    audio_extensions = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma')
    items = []
    if os.path.exists(directory_address) and os.path.isdir(directory_address):
        with os.scandir(directory_address) as entries:
            for entry in entries:
                if entry.is_dir():
                    items.append((entry.name, "Folder"))
                elif entry.is_file() and entry.name.lower().endswith(audio_extensions):
                    items.append((entry.name, "File"))
    else:
        items.append(("No items", "None"))

    return items
