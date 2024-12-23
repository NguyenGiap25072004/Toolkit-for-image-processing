# processing/color_processing.py
from PIL import Image, ImageEnhance  # Thêm ImageEnhance

def convert_to_grayscale(image):
    """
    Chuyển đổi ảnh sang ảnh grayscale.

    Args:
        image (PIL.Image): Ảnh đầu vào.

    Returns:
        PIL.Image: Ảnh đầu ra ở dạng grayscale.
    """
    return image.convert("L")

def adjust_brightness(image, factor):
    """
    Điều chỉnh độ sáng của ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        factor (float): Hệ số điều chỉnh độ sáng (0.0: tối đen, 1.0: giữ nguyên, >1.0: sáng hơn).

    Returns:
        PIL.Image: Ảnh đầu ra sau khi điều chỉnh độ sáng.
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def adjust_contrast(image, factor):
    """
    Điều chỉnh độ tương phản của ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        factor (float): Hệ số điều chỉnh độ tương phản (0.0: xám, 1.0: giữ nguyên, >1.0: tương phản hơn).

    Returns:
        PIL.Image: Ảnh đầu ra sau khi điều chỉnh độ tương phản.
    """
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def adjust_saturation(image, factor):
    """
    Điều chỉnh độ bão hòa của ảnh.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        factor (float): Hệ số điều chỉnh độ bão hòa (0.0: ảnh grayscale, 1.0: giữ nguyên, >1.0: bão hòa hơn).

    Returns:
        PIL.Image: Ảnh đầu ra sau khi điều chỉnh độ bão hòa.
    """
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)