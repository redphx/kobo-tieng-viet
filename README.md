> [!NOTE]
> *🇬🇧 If you want to create a new language pack for your language, check [redphx/kobo-language-pack](https://github.com/redphx/kobo-language-pack)*

# 🇻🇳 Dự án Kobo tiếng Việt
> [!IMPORTANT]
> Vui lòng chỉ chia sẻ link đến dự án thay vì tự ý upload lại bản cài đặt ở nơi khác. Cám ơn.

***Theo dõi Facebook của dự án: [fb.me/sachxy](https://fb.me/sachxy)***

Có ba vấn đề chính khi sử dụng máy đọc sách Kobo tại Việt Nam:  

1. Máy đọc được eBook tiếng Việt nhưng gặp lỗi hiển thị các phần như tiêu đề, mục lục...
2. Bàn phím không đủ ký tự tiếng Việt có dấu
3. Máy không hỗ trợ giao diện tiếng Việt (nếu người dùng cần)

Bản cài đặt ***hoàn toàn miễn phí*** này cung cấp giao diện tiếng Việt, thêm khả năng gõ tiếng Việt cho bàn phím và sửa lỗi hiển thị tiếng Việt trên các máy đọc sách Kobo.

## 🔥 1. Các tính năng của bản cài đặt
- Thêm ngôn ngữ tiếng Việt cho máy (vẫn có thể quay về giao diện tiếng Anh nếu muốn)
- Thêm khả năng gõ tiếng Việt cho bàn phím
- Sửa lỗi hiển thị tiếng Việt
- Sửa lỗi không hiển thị chính xác font monospace
- Dễ cài đặt, kích thước nhỏ gọn (bé hơn 3 MB)
- Hỗ trợ mọi dòng máy chạy firmware 4.x
- ***Tùy chọn:*** cài đặt thêm từ điển Anh-Việt Lạc Việt/TFlat 170 ngàn từ cho Kobo/Kindle tại [redphx/tudien](https://github.com/redphx/tudien)

Giao diện được dịch dựa trên bản dịch từ ChatGPT, sau đó được chỉnh sửa thủ công cho phù hợp.  
Bạn có thể đóng góp cho dự án bằng cách báo lỗi hoặc đề xuất cải thiện câu chữ của giao diện.  

Xin cảm ơn ♥️

| Trang chủ | Bàn phím tiếng Việt | Mục lục |
|:---------:|:---------:|:-------:|
| [![Trang chủ](docs/images/screenshot-home.png)](docs/images/screenshot-home.png) | [![Bàn phím tiếng Việt](docs/images/screenshot-keyboard.png)](docs/images/screenshot-activity.png) | [![Hoạt động](docs/images/screenshot-toc.png)](docs/images/screenshot-toc.png) |
| [redphx/tudien](https://github.com/redphx/tudien) | Font monospace | Chọn ngôn ngữ |
| [![Từ điển](docs/images/screenshot-dict.png)](docs/images/screenshot-dict.png) | [![Font monospace](docs/images/screenshot-monospace.png)](docs/images/screenshot-monospace.png) | [![Chọn ngôn ngữ](docs/images/screenshot-language.png)](docs/images/screenshot-language.png) |

## 🤓 2. Hướng dẫn cài đặt

Theo lý thuyết, bản cài đặt có thể dùng trên mọi máy Kobo chạy firmware 4.x. Không hỗ trợ firmware 3.x và 5.x.

***Đã xác nhận cài đặt thành công trên:***

- Aura (2013)  
- Clara 2E, BW, Colour, HD...  
- Libra 2, Colour...  

### Các bước cài đặt

> [!NOTE]
> Nên đọc mục ***3. Các câu hỏi thường gặp*** trước khi cài đặt.

1. Tải file [`KoboRoot.tgz`](https://github.com/redphx/kobo-tieng-viet/releases/latest) về máy
2. Kết nối Kobo với máy tính qua cổng USB, chép file `KoboRoot.tgz` vừa tải vào thư mục ẩn `.kobo` trên Kobo. Để nguyên, không giải nén, tên file phải là `KoboRoot.tgz`.
    > Nếu bạn dùng macOS và không thấy thư mục `.kobo`, nhấn tổ hợp phím `Cmd + Shift + .` để hiện thư mục ẩn trong Finder
3. Dùng chức năng `Tháo/Eject USB` trên máy tính để ngắt kết nối an toàn, tránh mất dữ liệu
4. Nếu làm đúng, Kobo sẽ tự động cập nhật và khởi động lại. Quá trình này chỉ mất tầm 3 phút. ***Không tắt nguồn khi máy đang cập nhật***.
5. Nếu xuất hiện hộp thoại như ảnh dưới, hãy khởi động máy lại để hoàn tất (giữ nút nguồn cho đến khi máy tắt hẳn, sau đó bật lại). Nếu không, bạn có thể bỏ qua bước này.
    > <img height="200" src="docs/images/screenshot-dialog.png" />
6. Máy sẽ tự động chuyển sang giao diện tiếng Việt. Nếu không, bạn có thể tự bật bằng cách:  
    `More > Settings > Language and dictionaries > Select your Language > Extra: vi`
7. ***Tùy chọn:*** cài đặt thêm từ điển Anh-Việt tổng hợp 170 ngàn từ tại [redphx/tudien](https://github.com/redphx/tudien)
8. Hoàn tất

Kể từ phiên bản `20260319`, máy sẽ tự động sửa lỗi tiếng Việt mỗi khi máy cập nhật lên firmware mới (xuất hiện hộp thoại như bước 5). Chỉ cần khởi động máy thêm một lần nữa là được.

### 🗑️ Gỡ bỏ

> Việc gỡ bỏ chỉ xóa tính năng tự sửa lỗi tiếng Việt + bàn phím tiếng Việt. Máy vẫn sẽ hiển thị tiếng Việt bình thường cho đến khi Factory Reset hoặc cài đặt lại firmware.

1. Kết nối Kobo với máy tính qua cổng USB
2. Tạo một file rỗng có tên `uninstall.txt` vào thư mục `.adds/tiengviet/`
3. Dùng chức năng `Tháo/Eject USB` trên máy tính để ngắt kết nối an toàn, tránh mất dữ liệu
4. Khởi động lại Kobo
5. Xóa thư mục `.adds/tiengviet/` (tùy chọn, không làm cũng được)


## 🙋 3. Các câu hỏi thường gặp

- **Cài đặt cái này có làm hư máy hay chậm máy không?**  
    > Bản cài đặt chỉ cập nhật font và thêm file ngôn ngữ tiếng Việt cho giao diện, không chỉnh sửa file hệ thống nên khả năng làm hư máy là gần như không có, và sẽ không làm máy chậm đi

- **Tôi có thể sử dụng bản cài đặt cho Kobo phiên bản nào?**
    > Bản cài đặt chỉ hỗ trợ máy chạy phiên bản 4.x (không hỗ trợ 3.x và 5.x)

- **Bản cài đặt có hỗ trợ các firmware phát hành sau này không?**
    > Bản cài đặt sẽ tự động hỗ trợ các firmware 4.x phát hành sau này

- **Sau khi cập nhật firmware mới cho Kobo tôi có phải cài đặt lại tiếng Việt không?**
    > Mỗi lần cập nhật firmware mới máy sẽ bị lỗi tiếng Việt trở lại. Chỉ cần khởi động máy một lần nữa là được, không cần cài lại Kobo Tiếng Việt.

- **Tôi đã cài bản [lelinhtinh/kobo-tieng-viet](https://github.com/lelinhtinh/kobo-tieng-viet), giờ có thể cài thêm bản này không?**
    > Hoàn toàn được, không lỗi lầm gì. Bạn chỉ cần làm theo hướng dẫn ở trên.

- **Tôi đã cài bản patch tiếng Việt của người khác làm, giờ có thể cài thêm bản này không?**
    > Mình không rõ các bản đó đã thay đổi những gì nên có thể sẽ không thể sử dụng chung được. Tốt nhất bạn nên reset về firmware gốc của máy, sau đó cài đặt lại bản này.

- **Làm sao để biết được phiên bản tiếng Việt đang cài đặt?**
    > Xem tại `Thêm > Cài đặt > Về Kobo`

## 📖 4. Thông tin font

Bản cài đặt này sẽ thay đổi các font mặc định của máy (không hỗ trợ tiếng Việt) thành các font khác (hỗ trợ tiếng Việt).

|                       | Font hệ thống                             | Font mới                                                             |
| ---------------------:| ----------------------------------------- | -------------------------------------------------------------------- |
| **Serif**             | Rakuten Serif<br>Georgia (firmware cũ)    | [Bitter](https://fonts.google.com/specimen/Bitter)                   |
| **Sans Serif**        | Rakuten Sans<br>Avenir Next (firmware cũ) | [Roboto](https://fonts.google.com/specimen/Roboto)                   |
| **Monospace**         | Không hỗ trợ (*)                          | [Source Code Pro](https://fonts.google.com/specimen/Source+Code+Pro) |
| **Hỗ trợ tiếng Việt** | ✗                                         | ✓                                                                    |

> (*) Khi một ePub dùng `font-family: monospace`, Kobo sẽ tìm một font hệ thống/tùy chọn bắt đầu bằng `Courier `. Tuy nhiên, Kobo không có font nào đáp ứng được tiêu chí trên nên việc hiển thị các chữ `monospace` bị sai. Để sửa lỗi này, bộ cài đặt sẽ chép các font cần thiết vào thư mục font tùy chọn `/fonts`.

Nếu không thích các font này, bạn có thể thay chúng bằng cách cập nhật font mới trong thư mục `fonts` (vẫn giữ nguyên tên), rồi làm theo hướng dẫn bên dưới để tạo lại bản cài đặt.

## 👩‍💻 5. Việc cần làm

- [ ] Cải thiện câu chữ
- [ ] GitHub Action để tự động build `KoboRoot.tgz`

## 🛠️ 6. Thông tin dành cho dev

### Hướng dẫn cách build

<details>
<summary>Build bản cài đặt chỉ có font</summary>

### Các bước để build

1. Cài [uv](https://docs.astral.sh/uv/) cho Python 3
2. Chạy lệnh để cài các package cần thiết:

    ```bash
    uv sync
    ```

3. Chạy lệnh để build file `dist/KoboRoot.tgz`:

    ```bash
    uv run python build-translations.py --include fonts
    ```

4. Cài file trên vào Kobo để thử nghiệm
</details>

<details>
<summary>Build bản cài đặt có cả bản dịch và font</summary>

### Chuẩn bị `lrelease`

Yêu cầu phải có tool `lrelease` của Qt để chuyển file dịch `.ts` sang `.qm`.  
Đã dùng thành công với [qt@5 trên macOS](https://formulae.brew.sh/formula/qt@5).

- **Windows:** [cài đặt Qt](https://www.qt.io/download-qt-installer-oss) rồi tìm file `lrelease.exe` trong thư mục cài đặt.

- **MacOS:**
    ```sh
    brew install qt@5
    ```

  File sẽ nằm ở vị trí `/opt/homebrew/opt/qt@5/bin/lrelease`

- **Linux:**  
    ```
    sudo apt-get install -y qttools5-dev-tools
    ```
  Sau đó dùng trực tiếp `lrelease`

Sau khi có được file `lrelease`, cấu hình đường dẫn của nó trong file `.env`

### Các bước để build

1. Cài [uv](https://docs.astral.sh/uv/) cho Python 3
2. Chạy lệnh để cài các package cần thiết:

    ```bash
    uv sync
    ```

3. Chạy lệnh để build file `dist/KoboRoot.tgz`:

    ```bash
    uv run python build-translations.py
    ```

4. Cài file trên vào Kobo để thử nghiệm
</details>

## 🤝 7. Lời cảm ơn
- ChatGPT đã hỗ trợ dịch
- [lelinhtinh/kobo-tieng-viet](https://github.com/lelinhtinh/kobo-tieng-viet) vì các thông tin về cách sửa lỗi font tiếng Việt
- [pipcat/kobo](https://github.com/pipcat/kobo) về tool để xuất file ngôn ngữ hệ thống từ firmware
