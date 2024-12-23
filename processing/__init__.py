# processing/__init__.py

# Có thể để trống hoặc import các module con
from .compression import *
from .enhancement import *
from .restoration import *
from .morphology import *
from .segmentation import *
from .utils import *
from .color_processing import *
# Hoặc import cụ thể các hàm:
# from .enhancement import histogram_equalization, clahe
# from .restoration import median_filter, wiener_filter
# ...