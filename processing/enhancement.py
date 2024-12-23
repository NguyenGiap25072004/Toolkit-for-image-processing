# processing/enhancement.py
import cv2
import numpy as np
from PIL import Image
from .utils import *

def histogram_equalization(image):
    """
    Thực hiện cân bằng lược đồ xám (Histogram Equalization).

    Args:
        image (PIL.Image): Ảnh đầu vào.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi cân bằng lược đồ xám.
    """
    img_yuv = cv2.cvtColor(pil_to_cv2(image), cv2.COLOR_RGB2YUV)
    img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    return cv2_to_pil(img_output)

def clahe(image, clip_limit=2.0, tile_grid_size=(8,8)):
    """
    Thực hiện cân bằng lược đồ xám thích nghi có giới hạn độ tương phản (CLAHE).

    Args:
        image (PIL.Image): Ảnh đầu vào.
        clip_limit (float): Ngưỡng giới hạn độ tương phản.
        tile_grid_size (tuple): Kích thước lưới ô.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi áp dụng CLAHE.
    """
    img_yuv = cv2.cvtColor(pil_to_cv2(image), cv2.COLOR_RGB2YUV)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    return cv2_to_pil(img_output)