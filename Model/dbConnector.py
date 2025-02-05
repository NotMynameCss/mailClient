import mysql.connector

# Kết nối MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Thay bằng user MySQL của bạn
        password="Ailienz_05",  # Thay bằng mật khẩu MySQL
        database="mail_client"
    )
