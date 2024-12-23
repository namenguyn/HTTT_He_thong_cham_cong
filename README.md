# Hệ thống chấm công

# Cài đặt workspace
- Cài MySQL tại đường link sau [MySQL Community Downloads](https://dev.mysql.com/downloads/mysql/) - Chọn phiên bản 8.4.3 LTS, tải về MSI Installer và làm theo video sau [Hướng dẫn cài MySQL](https://youtu.be/a3HJnbYhXUc).
- Vào Environment Variables trên máy, ở system variables, chọn Path, chọn Edit, chọn Browse, rồi chọn đến folder MySQL\MySQL Server 8.4\bin, sau đó nhấn OK.
- Test setup thành công bằng cách bật terminal/command prompt, chạy lệnh `mysql --version`.
  
# Cách chạy
## Clone git repo về máy
- Mở terminal, chạy lệnh `https://github.com/namenguyn/HTTT_He_thong_cham_cong.git`
## Chạy Backend
- Cd vào folder HTTT_He_thong_cham_cong, chạy lệnh `npm install` để cài các node_modules
- Chạy các file sql trong folder initializeTable_Data theo thứ tự đã đánh số để khởi tạo dữ liệu trên MySQL
- Ở folder HTTT_He_thong_cham_cong, tạo 1 file có tên `.env`, copy các dòng ở file `example_env.txt` sang file vừa tạo, thay đổi những chỗ cần thiết (như MYSQL_PASSWORD)
- Chạy `npm run dev` ở terminal trong folder HTTT_He_thong_cham_cong để khởi động server backend.
## Chạy Frontend
- Lưu ý cần chạy server backend trước khi chạy client frontend.
- Cd vào folder `HTTT_He_thong_cham_cong/frontend`, chạy `npm install` để cài các node_modules
- Sau khi cài xong, chạy lệnh `npm run dev` ở terminal đang trong folder `HTTT_He_thong_cham_cong/frontend` để khởi động client frontend.

 
