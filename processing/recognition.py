# processing/recognition.py
import cv2
import numpy as np
from .utils import pil_to_cv2, cv2_to_pil
from PIL import Image

def detect_faces(image):
    """
    Nhận dạng khuôn mặt sử dụng Haar Cascade.

    Args:
        image (PIL.Image): Ảnh đầu vào.

    Returns:
        PIL.Image: Ảnh đầu ra với các khuôn mặt được khoanh vùng.
    """
    img_cv = pil_to_cv2(image)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_RGB2GRAY)

    # Load the Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img_cv, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return cv2_to_pil(img_cv)