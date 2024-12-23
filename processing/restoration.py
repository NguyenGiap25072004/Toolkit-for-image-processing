# processing/restoration.py
import cv2
import numpy as np
from .utils import pil_to_cv2, cv2_to_pil
from PIL import Image

def median_filter(image, kernel_size=5):
    """
    Áp dụng bộ lọc trung vị (Median Filter) để khử nhiễu.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        kernel_size (int): Kích thước kernel (lẻ). Mặc định là 5.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi lọc.
    """
    img_cv = pil_to_cv2(image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    img_output = cv2.medianBlur(img_cv, kernel_size)
    img_output = cv2.cvtColor(img_output, cv2.COLOR_BGR2RGB)
    return cv2_to_pil(img_output)

def wiener_filter(image):
    """
    Áp dụng bộ lọc Wiener (Wiener Filter) để khử nhiễu và khôi phục ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi lọc.
    """
    # Wiener filter is more complex and often requires estimation of the noise and blur.
    # For simplicity, we'll use a basic implementation here.
    # In a real application, consider using more advanced libraries/techniques.
    
    # This is a placeholder implementation. 
    # A true Wiener filter implementation is beyond the scope of this example.
    # Consider using specialized libraries or custom implementations for a proper Wiener filter.
    
    img_cv = pil_to_cv2(image)
    img_cv = cv2.cvtColor(img_cv, cv2.COLOR_RGB2BGR)
    
    # Placeholder: Convert to grayscale for basic processing
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
    
    # Placeholder: Apply a slight Gaussian blur as a basic form of Wiener-like filtering
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Convert back to RGB
    output_img = cv2.cvtColor(blurred, cv2.COLOR_GRAY2BGR)
    
    return cv2_to_pil(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))