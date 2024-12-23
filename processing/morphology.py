# processing/morphology.py
import cv2
import numpy as np
from .utils import pil_to_cv2, cv2_to_pil
from PIL import Image

def erosion(image, kernel_size=3, iterations=1):
    """
    Thực hiện phép co (erosion) ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.
        iterations (int): Số lần lặp lại phép co. Mặc định là 1.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi thực hiện phép co.
    """
    img_cv = pil_to_cv2(image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img_output = cv2.erode(img_cv, kernel, iterations=iterations)
    img_output = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
    return cv2_to_pil(img_output)

def dilation(image, kernel_size=3, iterations=1):
    """
    Thực hiện phép giãn (dilation) ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.
        iterations (int): Số lần lặp lại phép giãn. Mặc định là 1.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi thực hiện phép giãn.
    """
    img_cv = pil_to_cv2(image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img_output = cv2.dilate(img_cv, kernel, iterations=iterations)
    img_output = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
    return cv2_to_pil(img_output)

def opening(image, kernel_size=3):
    """
    Thực hiện phép mở (opening) ảnh (erosion sau đó dilation).

    Args:
        image (PIL.Image): Ảnh đầu vào.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi thực hiện phép mở.
    """
    img_cv = pil_to_cv2(image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img_output = cv2.morphologyEx(img_cv, cv2.MORPH_OPEN, kernel)
    img_output = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
    return cv2_to_pil(img_output)

def closing(image, kernel_size=3):
    """
    Thực hiện phép đóng (closing) ảnh (dilation sau đó erosion).

    Args:
        image (PIL.Image): Ảnh đầu vào.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 3.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi thực hiện phép đóng.
    """
    img_cv = pil_to_cv2(image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    img_output = cv2.morphologyEx(img_cv, cv2.MORPH_CLOSE, kernel)
    img_output = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
    return cv2_to_pil(img_output)