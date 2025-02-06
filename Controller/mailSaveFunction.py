# Khắc phục lỗi đường dẫn, đảm bảo đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Kết nối CSDL
import Model.dbConnector as dbconnect

# Lưu email vào MySQL
def save_email(sender, receiver, subject, body):
    try:
        conn = dbconnect.connect_db()
        cursor = conn.cursor()
        sql = "INSERT INTO emails (sender, receiver, subject, body) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (sender, receiver, subject, body))
        conn.commit()
        conn.close()
        print("✅ Email đã lưu vào MySQL!")
    except Exception as e:
        print(f"❌ Lỗi lưu email vào MySQL: {e}")