# gui/main_window.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

from gui.image_viewer import ImageViewer
from gui.info_panel import InfoPanel
from gui.processing_panel import ProcessingPanel
from processing import compression, enhancement, restoration, morphology, segmentation, recognition, color_processing

class MainWindow(ThemedTk):
    def __init__(self):
        super().__init__(theme="breeze")  # Chọn theme từ ttkthemes
        self.title("Image Processing App")
        self.geometry("1000x700")
        self.compression_functions = {
            "JPEG Compression": compression.compress_jpeg,
            "PNG Compression": compression.compress_png,
        }
        self.color_processing_functions = {
            "Convert to Grayscale": color_processing.convert_to_grayscale,
            "Adjust Brightness": color_processing.adjust_brightness,
            "Adjust Contrast": color_processing.adjust_contrast,
            "Adjust Saturation": color_processing.adjust_saturation,
        }
        # Icon
        try:
            self.iconbitmap("assets/icon.ico")
        except tk.TclError:
            print("Warning: Could not load icon file.")

        # Menu Bar (Optional)
        self.create_menu_bar()

        # Toolbar (Optional)
        # ...

        # Left Panel
        self.left_panel = tk.Frame(self)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        self.info_panel = InfoPanel(self.left_panel)
        self.info_panel.pack(fill=tk.X)

        self.processing_panel = ProcessingPanel(self.left_panel, self)
        self.processing_panel.pack(fill=tk.BOTH, expand=True)

        # Center Panel
        self.center_panel = tk.Frame(self)
        self.center_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.image_viewer = ImageViewer(self.center_panel)
        self.image_viewer.pack(fill=tk.BOTH, expand=True)

        # Status Bar (Optional)
        self.status_bar = tk.Label(self, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Gắn các hàm xử lý từ processing module vào MainWindow
        self.enhancement_functions = {
            "Histogram Equalization": enhancement.histogram_equalization,
            "CLAHE": enhancement.clahe,
        }
        self.restoration_functions = {
            "Median Filter": restoration.median_filter,
            "Wiener Filter": restoration.wiener_filter,
        }
        self.morphology_functions = {
            "Erosion": morphology.erosion,
            "Dilation": morphology.dilation,
            "Opening": morphology.opening,
            "Closing": morphology.closing,
        }
        self.segmentation_functions = {
            "Thresholding": segmentation.thresholding,
            "Canny Edge Detection": segmentation.canny_edge_detection,
        }
        self.recognition_functions = {
            "Detect Faces": recognition.detect_faces,
        }

        # Gọi hàm để tạo các nút xử lý trong ProcessingPanel
        self.processing_panel.create_buttons()

    def create_menu_bar(self):
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Load Image", command=self.load_image)
        filemenu.add_command(label="Save Image", command=self.image_viewer.save_image)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.quit)

        helpmenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self.show_about)

    def load_image(self):
        filepath = filedialog.askopenfilename(
            initialdir="./",
            title="Select Image",
            filetypes=(
                ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.ico"),
                ("All files", "*.*"),
            ),
        )
        if filepath:
            self.image_viewer.load_image(filepath)
            self.info_panel.update_info(filepath, self.image_viewer.original_image)

    def apply_enhancement(self, func_name):
        self.apply_processing(self.enhancement_functions, func_name)

    def apply_restoration(self, func_name):
        self.apply_processing(self.restoration_functions, func_name)

    def apply_morphology(self, func_name):
        self.apply_processing(self.morphology_functions, func_name)

    def apply_segmentation(self, func_name):
        self.apply_processing(self.segmentation_functions, func_name)
        
    def apply_recognition(self, func_name):
        self.apply_processing(self.recognition_functions, func_name)

    def apply_processing(self, functions, func_name):
        if self.image_viewer.original_image:
            try:
                processed_image = functions[func_name](self.image_viewer.original_image)
                self.image_viewer.update_processed_image(processed_image)
                self.status_bar.config(text=f"Applied {func_name}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during processing: {e}")
    def apply_compression(self, func_name):
        if self.image_viewer.original_image:
            try:
                processed_image = self.compression_functions[func_name](self.image_viewer.original_image)
                self.image_viewer.update_processed_image(processed_image)
                self.status_bar.config(text=f"Applied {func_name}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during processing: {e}")
    
    def apply_color_processing(self, func_name):
        if self.image_viewer.original_image:
            try:
                # Xử lý đặc biệt cho các hàm cần tham số factor
                if func_name in ["Adjust Brightness", "Adjust Contrast", "Adjust Saturation"]:
                    # Mở hộp thoại hỏi người dùng nhập factor
                    factor = tk.simpledialog.askfloat("Input", f"Enter factor for {func_name}:", minvalue=0.0, maxvalue=3.0, initialvalue=1.0)
                    if factor is None:
                        return # Người dùng đã hủy
                    processed_image = self.color_processing_functions[func_name](self.image_viewer.original_image, factor)

                else:
                    processed_image = self.color_processing_functions[func_name](self.image_viewer.original_image)
                self.image_viewer.update_processed_image(processed_image)
                self.status_bar.config(text=f"Applied {func_name}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during processing: {e}")
    def show_about(self):
        messagebox.showinfo("About", "Image Processing App\nVersion 1.0\nDeveloped by Nguyen Huu Giap")