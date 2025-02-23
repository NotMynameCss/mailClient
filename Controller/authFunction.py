## FILE: (Xử lý xác thực Gmail)

# Thêm thư mục gốc của dự án vào sys.path: sử dụng để đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# chức năng login
import smtplib
import imaplib
import Config.config as config

def login_gmail(email, password):
    try:
        smtp = smtplib.SMTP(config.GMAIL_SMTP_SERVER, config.GMAIL_SMTP_PORT)
        smtp.starttls()
        smtp.login(email, password)
        return smtp

        # Kiểm tra đăng nhập IMAP(nhận mail)
        imap = imaplib.IMAP4_SSL(config.GMAIL_IMAP_SERVER, config.GMAIL_IMAP_PORT)
        imap.login(email, password)
        imap.logout()

        return True # Login success
        print(f" đăng nhập Success: {e}")
    except Exception as e:
        print(f"❌ Lỗi đăng nhập: {e}")
        return False # Login failed