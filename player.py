import os
from pygame import mixer

class MusicPlayer:
    def __init__(self):
        mixer.init()
        self.current_song = None
        self.song_queue = []
        self.paused = False

    def load_music(self, directory):
        self.song_queue = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp3', '.wav'))]
        print("Music loaded.")

    def play_song(self, song):
        if self.current_song:
            mixer.music.pause()
        mixer.music.load(song)
        mixer.music.play()
        self.current_song = song
        self.paused = False
        print(f"Playing: {os.path.basename(song)}")

    def pause_song(self):
        if self.paused == False:
            mixer.music.pause()
            self.paused = True
        else:
            mixer.music.unpause()
            self.paused = False