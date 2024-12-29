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
- **Xử lý ảnh màu (Color Image Processing):**
  - Chuyển đổi ảnh màu sang ảnh đa mức xám (grayscale).
  - Điều chỉnh độ sáng của ảnh (Adjust Brightness).
  - Điều chỉnh độ tương phản của ảnh (Adjust Contrast).
  - Điều chỉnh độ bão hòa màu của ảnh (Adjust Saturation).
- **Nén ảnh (Image Compression):**
  - (Nén ảnh mất dữ liệu) - JPEG (Joint Photographic Experts Group)
  - (Nén ảnh không mất dữ liệu) - PNG (Portable Network Graphics)

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
    - Chọn nhóm chức năng (Enhancement, Restoration, Morphology, Segmentation, Recognition, Color Processing, Compression).
    - Nhấn nút của chức năng tương ứng để áp dụng cho ảnh.
4.  **Lưu ảnh:** Nhấn `File` -> `Save Image` hoặc nhấn nút `Save Image` trên giao diện và chọn nơi lưu ảnh đã xử lý.

## Cấu trúc thư mục

![Screenshot 2024-12-23 092228](https://github.com/user-attachments/assets/cf56eaa5-70e7-45b5-a28e-aaffb33a05de)


## Phiên bản

*   Phiên bản 1.0

## Tác giả

*   Nguyễn Hữu Giáp - 22110120@st.vju.ac.vn

## Ghi chú

*   Phần nhận dạng đối tượng (Recognition) hiện tại chỉ triển khai nhận diện khuôn mặt đơn giản sử dụng Haar Cascade.
*   Bộ lọc Wiener (Wiener Filter) trong phần khôi phục ảnh (Restoration) chỉ là triển khai cơ bản cho mục đích minh họa. Triển khai đầy đủ phức tạp hơn và đòi hỏi ước lượng hàm truyền đạt nhiễu và hàm truyền đạt của quá trình làm mờ ảnh.
*   Ứng dụng sử dụng theme `breeze` từ thư viện `ttkthemes`. Bạn có thể thay đổi theme khác trong file `main.py`.
