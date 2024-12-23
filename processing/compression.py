# processing/compression.py
from PIL import Image
import io

def compress_jpeg(image, quality=75):
    """
    Nén ảnh sử dụng phương pháp JPEG.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        quality (int): Chất lượng nén (0-100, mặc định là 75).

    Returns:
        PIL.Image: Ảnh đầu ra sau khi nén.
    """
    # Lưu ảnh vào bộ nhớ đệm với định dạng JPEG
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='JPEG', quality=quality)
    img_byte_arr = img_byte_arr.getvalue()

    # Đọc ảnh đã nén từ bộ nhớ đệm
    compressed_image = Image.open(io.BytesIO(img_byte_arr))
    return compressed_image

def compress_png(image, compress_level=6):
    """
    Nén ảnh sử dụng phương pháp PNG.

    Args:
        image (PIL.Image): Ảnh đầu vào.
        compress_level (int): Mức độ nén (0-9, mặc định là 6).

    Returns:
        PIL.Image: Ảnh đầu ra sau khi nén.
    """
    # Lưu ảnh vào bộ nhớ đệm với định dạng PNG
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG', compress_level=compress_level)
    img_byte_arr = img_byte_arr.getvalue()

    # Đọc ảnh đã nén từ bộ nhớ đệm
    compressed_image = Image.open(io.BytesIO(img_byte_arr))
    return compressed_image