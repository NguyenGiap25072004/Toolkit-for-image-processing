# gui/info_panel.py
import tkinter as tk
from tkinter import ttk
import os

class InfoPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.filepath_label = ttk.Label(self, text="File: N/A")
        self.filepath_label.pack(fill=tk.X)

        self.resolution_label = ttk.Label(self, text="Resolution: N/A")
        self.resolution_label.pack(fill=tk.X)

        self.size_label = ttk.Label(self, text="Size: N/A")
        self.size_label.pack(fill=tk.X)

    def update_info(self, filepath, image):
        filename = os.path.basename(filepath)
        self.filepath_label.config(text=f"File: {filename}")

        if image:
            resolution = f"{image.width} x {image.height}"
            self.resolution_label.config(text=f"Resolution: {resolution}")

            file_size = os.path.getsize(filepath) / 1024  # Size in KB
            self.size_label.config(text=f"Size: {file_size:.2f} KB")
        else:
            self.resolution_label.config(text="Resolution: N/A")
            self.size_label.config(text="Size: N/A")