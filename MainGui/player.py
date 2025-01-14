import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music Player")
        self.master.geometry("300x300")
        
        self.music_files = []  # List to store music files
        self.selected_file_index = None
        self.playing = False
        self.paused_position = 0  # Variable to store the position when music is paused
        
        self.create_widgets()
        
    def create_widgets(self):
        self.listbox = tk.Listbox(self.master)
        self.listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
        
        self.load_button = tk.Button(self.master, text="Load Music Files", command=self.load_music_files)
        self.load_button.pack(pady=5)
        
        self.play_button = tk.Button(self.master, text="Play", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_music, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
    def load_music_files(self):
        self.music_files = filedialog.askopenfilenames(defaultextension=".mp3", filetypes=[("Music files", "*.mp3")])
        for file in self.music_files:
            filename = os.path.basename(file)
            self.listbox.insert(tk.END, filename)
        
        if self.music_files:
            self.play_button.config(state=tk.NORMAL)
        
    def play_music(self):
        if not self.playing and self.music_files:
            if self.paused_position == 0:  # If music is not paused, start from beginning
                self.selected_file_index = self.listbox.curselection()[0]
                selected_file = self.music_files[self.selected_file_index]
                pygame.mixer.init()
                pygame.mixer.music.load(selected_file)
                pygame.mixer.music.play()
            else:  # If music is paused, resume from the paused position
                pygame.mixer.music.unpause()
                
            self.playing = True
            self.play_button.config(text="Pause")
            self.stop_button.config(state=tk.NORMAL)
        else:
            pygame.mixer.music.pause()
            self.playing = False
            self.paused_position = pygame.mixer.music.get_pos()  # Store the current position
            self.play_button.config(text="Play")
        
    def stop_music(self):
        pygame.mixer.music.stop()
        self.play_button.config(text="Play")
        self.playing = False
        self.paused_position = 0  # Reset the paused position

