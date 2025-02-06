# Khắc phục lỗi đường dẫn, đảm bảo đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# kết nối CSDL
import Model.dbConnector as dbconnect

def search_emails(keyword):
    try:
        conn = dbconnect.connect_db()
        cursor = conn.cursor()
        sql = """
            SELECT id, sender, subject, timestamp
            FROM emails
            WHERE sender LIKE %s OR subject LIKE %s OR body LIKE %s
            ORDER BY timestamp DESC
            """
        cursor.execute(sql, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))
        
        emails = cursor.fetchall()
        conn.close()
        return emails
    except Exception as e:
        print(f"❌ Lỗi tìm kiếm email: {e}")