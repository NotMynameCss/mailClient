# Thêm thư mục gốc của dự án vào sys.path: sử dụng để đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# kết nối CSDL 
import Model.dbConnector as dbconnect



# Lấy nội dung chi tiết email
def fetch_email_details(email_id):
    conn = dbconnect.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT sender, receiver, subject, body, timestamp FROM emails WHERE id = %s", (email_id,))
    email_details = cursor.fetchone()
    conn.close()
    return email_details