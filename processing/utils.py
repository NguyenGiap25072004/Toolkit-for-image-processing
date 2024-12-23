# processing/utils.py
import cv2
import numpy as np
from PIL import Image

def pil_to_cv2(image):
    """
    Chuyển đổi ảnh từ định dạng PIL Image sang OpenCV (NumPy array).

    Args:
        image (PIL.Image): Ảnh đầu vào.

    Returns:
        numpy.ndarray: Ảnh đầu ra ở định dạng OpenCV.
    """
    return np.array(image)

def cv2_to_pil(image):
    """
    Chuyển đổi ảnh từ định dạng OpenCV (NumPy array) sang PIL Image.

    Args:
        image (numpy.ndarray): Ảnh đầu vào.

    Returns:
        PIL.Image: Ảnh đầu ra ở định dạng PIL.
    """
    return Image.fromarray(image)

def resize_image(image, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Thay đổi kích thước ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        width (int): Chiều rộng mong muốn.
        height (int): Chiều cao mong muốn.
        inter (int): Phương pháp nội suy. Mặc định là cv2.INTER_AREA (tốt cho thu nhỏ).

    Returns:
        PIL.Image: Ảnh đầu ra sau khi thay đổi kích thước.
    """
    
    # Nếu cả width và height đều không được cung cấp thì giữ nguyên ảnh gốc
    if width is None and height is None:
        return image

    # Tính toán tỉ lệ khung hình và kích thước mới
    (h, w) = image.size
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))
    
    # Chuyển đổi sang OpenCV image để resize
    img_cv = pil_to_cv2(image)
    
    # Resize ảnh
    resized = cv2.resize(img_cv, dim, interpolation=inter)
    
    # Chuyển đổi lại sang PIL Image
    return cv2_to_pil(resized)

def rgb_to_grayscale(image):
    """
    Chuyển đổi ảnh RGB sang ảnh grayscale.

    Args:
        image (PIL.Image): Ảnh đầu vào.

    Returns:
        PIL.Image: Ảnh đầu ra ở dạng grayscale.
    """
    return image.convert("L")

def rotate_image(image, angle):
    """
    Xoay ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        angle (float): Góc xoay (độ).

    Returns:
        PIL.Image: Ảnh đầu ra sau khi xoay.
    """
    return image.rotate(angle)

def flip_image(image, mode):
    """
    Lật ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        mode (str): 'horizontal' hoặc 'vertical'.

    Returns:
        PIL.Image: Ảnh đầu ra sau khi lật.
    """
    if mode == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    elif mode == 'vertical':
        return image.transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Invalid mode. Choose 'horizontal' or 'vertical'.")