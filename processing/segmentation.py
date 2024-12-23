# processing/segmentation.py
import cv2
import numpy as np
from .utils import pil_to_cv2, cv2_to_pil
from PIL import Image

def thresholding(image, threshold_value=127, max_value=255, method=cv2.THRESH_BINARY):
    """
    Phân ngưỡng ảnh (Thresholding).

    Args:
        image (PIL.Image): Ảnh đầu vào.
        threshold_value (int): Ngưỡng phân loại. Mặc định là 127.
        max_value (int): Giá trị pixel lớn nhất sau khi phân ngưỡng. Mặc định là 255.
        method (int): Phương pháp phân ngưỡng. Mặc định là cv2.THRESH_BINARY.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi phân ngưỡng.
    """
    img_cv = pil_to_cv2(image)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
    ret, img_output = cv2.threshold(gray, threshold_value, max_value, method)
    img_output = cv2.cvtColor(img_output, cv2.COLOR_GRAY2RGB)
    return cv2_to_pil(img_output)

def canny_edge_detection(image, threshold1=100, threshold2=200):
    """
    Phát hiện biên sử dụng thuật toán Canny.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        threshold1 (int): Ngưỡng thấp cho hysteresis. Mặc định là 100.
        threshold2 (int): Ngưỡng cao cho hysteresis. Mặc định là 200.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi phát hiện biên.
    """
    img_cv = pil_to_cv2(image)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    img_output = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    return cv2_to_pil(img_output)