# Image Processing App

Đây là một ứng dụng xử lý ảnh đơn giản được xây dựng bằng Python, sử dụng các thư viện như Tkinter, Pillow, OpenCV và NumPy. Ứng dụng cung cấp giao diện đồ họa (GUI) cho phép người dùng thực hiện các thao tác xử lý ảnh cơ bản.

## Tính năng

- **Tăng cường chất lượng ảnh (Enhancement):**
  - Cân bằng lược đồ xám (Histogram Equalization)
  - Cân bằng lược đồ xám thích nghi có giới hạn độ tương phản (CLAHE)
- **Khôi phục ảnh (Restoration):**
  - Lọc trung vị (Median Filter)
  - Lọc Wiener (Wiener Filter) - _Lưu ý: Triển khai cơ bản_
- **Xử lý hình thái học (Morphology):**
  - Phép co (Erosion)
  - Phép giãn (Dilation)
  - Phép mở (Opening)
  - Phép đóng (Closing)
- **Phân vùng ảnh (Segmentation):**
  - Phân ngưỡng (Thresholding)
  - Phát hiện biên Canny (Canny Edge Detection)
- **Nhận dạng đối tượng (Recognition):**
  - Nhận diện khuôn mặt (Detect Faces) - _Sử dụng Haar Cascade_

## Cài đặt

1.  **Yêu cầu:**
    - Python 3.x
2.  **Tạo môi trường ảo (đề xuất):**
    ```bash
    python3 -m venv venv
    ```
    Kích hoạt môi trường ảo:
    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```
3.  **Cài đặt các thư viện cần thiết:**
    ```bash
    pip install -r requirements.txt
    ```

## Hướng dẫn sử dụng

1.  Chạy file `main.py`:
    ```bash
    python main.py
    ```
2.  **Load ảnh:** Nhấn `File` -> `Load Image` hoặc nhấn nút `Load Image` trên giao diện và chọn file ảnh bạn muốn xử lý.
3.  **Chọn chức năng xử lý:**
    - Chọn nhóm chức năng (Enhancement, Restoration, Morphology, Segmentation, Recognition).
    - Nhấn nút của chức năng tương ứng để áp dụng cho ảnh.
4.  **Lưu ảnh:** Nhấn `File` -> `Save Image` hoặc nhấn nút `Save Image` trên giao diện và chọn nơi lưu ảnh đã xử lý.

## Cấu trúc thư mục
image_processing_app/
├── main.py             # File chạy chính, khởi tạo GUI
├── gui/                # Module giao diện người dùng
│   ├── init.py
│   ├── main_window.py   # Lớp giao diện chính
│   ├── image_viewer.py # Lớp hiển thị ảnh
│   ├── info_panel.py   # Lớp hiển thị thông tin ảnh
│   └── processing_panel.py # Lớp chứa các nút xử lý
├── processing/         # Module xử lý ảnh
│   ├── init.py
│   ├── enhancement.py  # Các thuật toán tăng cường chất lượng ảnh
│   ├── restoration.py  # Các thuật toán khôi phục ảnh
│   ├── morphology.py   # Các thuật toán xử lý hình thái học
│   ├── segmentation.py # Các thuật toán phân vùng ảnh
│   ├── recognition.py  # Các thuật toán nhận dạng đối tượng
│   └── utils.py        # Các hàm tiện ích cho xử lý ảnh
├── assets/             # Thư mục chứa tài nguyên (icon, hình ảnh,...)
│   └── icon.ico        # Icon của ứng dụng
├── requirements.txt    # Danh sách các thư viện cần thiết
└── README.md           # File hướng dẫn này

## Phiên bản

*   Phiên bản 1.0

## Tác giả

*   \[Tên của bạn] - \[Email của bạn]

## Ghi chú

*   Phần nhận dạng đối tượng (Recognition) hiện tại chỉ triển khai nhận diện khuôn mặt đơn giản sử dụng Haar Cascade.
*   Bộ lọc Wiener (Wiener Filter) trong phần khôi phục ảnh (Restoration) chỉ là triển khai cơ bản cho mục đích minh họa. Triển khai đầy đủ phức tạp hơn và đòi hỏi ước lượng hàm truyền đạt nhiễu và hàm truyền đạt của quá trình làm mờ ảnh.
*   Để phát triển các tính năng nhận dạng đối tượng nâng cao, bạn có thể tham khảo các thư viện học sâu như TensorFlow, PyTorch.
*   Ứng dụng sử dụng theme `breeze` từ thư viện `ttkthemes`. Bạn có thể thay đổi theme khác trong file `main.py`.

## Giấy phép

Dự án này được cấp phép theo giấy phép \[Tên giấy phép] - xem file `LICENSE` để biết thêm chi tiết (nếu có).