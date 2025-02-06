# Khắc phục lỗi đường dẫn, đảm bảo đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Kết nối CSDL
import Model.dbConnector as dbconnect

# Xóa email khỏi MySQL
def delete_email(email_id):
    try:
        conn = dbconnect.connect_db()
        cursor = conn.cursor()
        sql = "DELETE FROM emails WHERE id = %s" # sử dụng parameterized query( %s ) thay vì ghép chuỗi trực tiếp để chống SQL injection
        cursor.execute(sql, (email_id,))
        conn.commit()
        conn.close()
        print("✅ Email đã được xóa khỏi MySQL!")
    except Exception as e:
        print(f"❌ Lỗi xóa email: {e}")

