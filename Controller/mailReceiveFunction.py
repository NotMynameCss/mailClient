import imaplib
import email

# Thống tin tài khoản gmail
EMAIL_SENDER = "modpackphieuluu@gmail.com"
PASSWORD_SENDER = "gxqp sfjo ptem yyln"

def fetch_emails():
    try:
        # Kết nối Mail IMAP server
        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        mail.login(EMAIL_SENDER, PASSWORD_SENDER)
        mail.select("INBOX")

        # Lấy danh sách email chưa đọc
        result, email_data = mail.search(None, "ALL")
        email_ids = email_data[0].split()

        print(f"tìm thấy {len(email_ids)}: email")

        # đọc email mới nhất
        last_email_id = email_ids[-1]
        result, email_data = mail.fetch(last_email_id, "(RFC822)")
        raw_email = email_data[0][1]

        # phân tích nội dung email từ byte sang email.message.eMailMessage
        
        msg = email.message_from_bytes(raw_email)
        subject = msg["Subject"]
        sender = msg["From"]
        print(f"From: {sender}")
        print(f"Subject: {subject}")

        # đọc nội dung email
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode("utf-8")
                    print(f"Body: {body}")
        else:
            print(f"Body: {msg.get_payload(decode=True).decode("utf-8")}")

        mail.logout()

    except Exception as e:
        print(f"lỗi nhận mail: {e}")            

fetch_emails()