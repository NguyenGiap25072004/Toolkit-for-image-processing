# gui/image_viewer.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk

class ImageViewer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.image_path = ""
        self.original_image = None
        self.processed_image = None
        self.processed_photo = None

        self.canvas_original = tk.Canvas(self, width=400, height=300, bg="gray")
        self.canvas_original.pack(side=tk.LEFT, padx=5, pady=5)

        self.canvas_processed = tk.Canvas(self, width=400, height=300, bg="gray")
        self.canvas_processed.pack(side=tk.LEFT, padx=5, pady=5)

    def load_image(self, image_path):
        try:
            self.image_path = image_path
            self.original_image = Image.open(image_path)
            self.processed_image = self.original_image.copy()

            self.display_image(self.original_image, self.canvas_original)
            self.display_image(self.processed_image, self.canvas_processed)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {e}")

    def display_image(self, image, canvas):
        canvas.delete("all")  # Clear the canvas
        
        # Resize image to fit canvas while maintaining aspect ratio
        width, height = image.size
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()

        if width > canvas_width or height > canvas_height:
            if width / canvas_width > height / canvas_height:
                new_width = canvas_width
                new_height = int(height * (canvas_width / width))
            else:
                new_height = canvas_height
                new_width = int(width * (canvas_height / height))
            image = image.resize((new_width, new_height), Image.LANCZOS)

        photo = ImageTk.PhotoImage(image)
        canvas.create_image(canvas_width / 2, canvas_height / 2, anchor=tk.CENTER, image=photo)
        canvas.image = photo

    def update_processed_image(self, processed_image):
        self.processed_image = processed_image
        self.display_image(self.processed_image, self.canvas_processed)

    def save_image(self):
        if self.processed_image:
            save_path = filedialog.asksaveasfilename(
                initialdir="./",
                title="Save Image As",
                defaultextension=".png",
                filetypes=(
                    ("PNG", "*.png"),
                    ("JPEG", "*.jpg *.jpeg"),
                    ("BMP", "*.bmp"),
                    ("All Files", "*.*"),
                ),
            )
            if save_path:
                try:
                    self.processed_image.save(save_path)
                    messagebox.showinfo("Success", "Image saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image: {e}")
    
    def clear_canvas(self, canvas):
        canvas.delete("all")