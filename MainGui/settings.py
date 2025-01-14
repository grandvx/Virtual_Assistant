import tkinter as tk
import pygame
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class DeviceSettings:
    def __init__(self, master):
        self.master = master
        self.master.title("Device Settings")
        self.master.geometry("300x150")
        
        pygame.mixer.init()  # Initialize mixer
        
        self.volume_scale = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, label="Volume", command=self.adjust_volume)
        self.volume_scale.pack(pady=10, padx=20, fill=tk.X)
        
        self.update_volume_display()  # Update the volume display
        
    def adjust_volume(self, volume):
        volume_level = float(volume) / 100
        self.set_system_volume(volume_level)
        
    def set_system_volume(self, volume_level):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(volume_level, None)
        
    def update_volume_display(self):
        current_volume = pygame.mixer.music.get_volume() * 100
        self.volume_scale.set(int(current_volume))  # Update scale position with current volume

