# Thêm thư mục gốc của dự án vào sys.path: sử dụng để đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ket nối CSDL
import mysql.connector

# Kết nối MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Thay bằng user MySQL của bạn
        password="Ailienz_05",  # Thay bằng mật khẩu MySQL
        database="mail_client"
    )
