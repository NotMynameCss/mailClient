# Khắc phục lỗi đường dẫn, đảm bảo đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# kết nối CSDL
import Model.dbConnector as dbconnect

################### bản gốc
def fetch_emails(email):
    conn = dbconnect.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, sender, subject, timestamp FROM emails ORDER BY timestamp DESC")
    emails = cursor.fetchall()
    conn.close()
    return emails

