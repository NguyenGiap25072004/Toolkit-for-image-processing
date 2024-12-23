import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # Thêm import

class ProcessingPanel(tk.Frame):
    def __init__(self, master, main_window):
        super().__init__(master)
        self.main_window = main_window

        # Tạo Canvas để chứa các nút
        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Tạo Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Liên kết Scrollbar với Canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Tạo Frame bên trong Canvas để chứa các nút
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.create_buttons()

    def create_buttons(self):
        # Enhancement
        self.create_button_group("Enhancement", self.main_window.enhancement_functions)

        # Restoration
        self.create_button_group("Restoration", self.main_window.restoration_functions)

        # Morphology
        self.create_button_group("Morphology", self.main_window.morphology_functions)

        # Segmentation
        self.create_button_group("Segmentation", self.main_window.segmentation_functions)

        # Recognition
        self.create_button_group("Recognition", self.main_window.recognition_functions)

        # Compression
        self.create_button_group("Compression", self.main_window.compression_functions)

        # Color Processing
        self.create_button_group("Color Processing", self.main_window.color_processing_functions)

    def create_button_group(self, group_name, functions):
        # Tạo Label cho nhóm
        group_label = ttk.Label(self.frame, text=group_name + ":")
        group_label.pack(pady=(20, 5))

        # Tạo các nút cho nhóm
        for func_name in functions:
            if func_name == "JPEG Compression":
                # Tạo PhotoImage từ icon
                zoom_in_icon = Image.open(
                    "assets/zoom-in.png"
                )  # Thay "assets/zoom-in.png" bằng đường dẫn đến icon của bạn
                zoom_in_icon = zoom_in_icon.resize((20, 20), Image.LANCZOS)  # Resize icon
                zoom_in_photo = ImageTk.PhotoImage(zoom_in_icon)

                button = ttk.Button(
                    self.frame,
                    text=func_name,
                    image=zoom_in_photo,
                    compound="left",  # Để icon hiển thị bên trái chữ
                    command=lambda name=func_name: self.apply_processing(group_name, name),
                )
                button.image = zoom_in_photo
                button.pack(fill=tk.X, padx=5, pady=2)
            elif func_name == "PNG Compression":
                # Tạo PhotoImage từ icon
                zoom_out_icon = Image.open(
                    "assets/zoom-out.png"
                )  # Thay "assets/zoom-out.png" bằng đường dẫn đến icon của bạn
                zoom_out_icon = zoom_out_icon.resize((20, 20), Image.LANCZOS)
                zoom_out_photo = ImageTk.PhotoImage(zoom_out_icon)

                button = ttk.Button(
                    self.frame,
                    text=func_name,
                    image=zoom_out_photo,
                    compound="left",  # Để icon hiển thị bên trái chữ
                    command=lambda name=func_name: self.apply_processing(group_name, name),
                )
                button.image = (
                    zoom_out_photo
                )  # Giữ tham chiếu để tránh bị garbage collected
                button.pack(fill=tk.X, padx=5, pady=2)
            else:
                button = ttk.Button(
                    self.frame,
                    text=func_name,
                    command=lambda name=func_name: self.apply_processing(
                        group_name, name
                    ),
                )
                button.pack(fill=tk.X, padx=5, pady=2)

    def apply_processing(self, group_name, func_name):
        if group_name == "Enhancement":
            self.main_window.apply_enhancement(func_name)
        elif group_name == "Restoration":
            self.main_window.apply_restoration(func_name)
        elif group_name == "Morphology":
            self.main_window.apply_morphology(func_name)
        elif group_name == "Segmentation":
            self.main_window.apply_segmentation(func_name)
        elif group_name == "Recognition":
            self.main_window.apply_recognition(func_name)
        elif group_name == "Compression":
            self.main_window.apply_compression(func_name)
        elif group_name == "Color Processing":
            self.main_window.apply_color_processing(func_name)