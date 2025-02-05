# kết nối CSDL
import dbConnector as dbconnect
# dùng cho gửi email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# dùng cho nhận email
import imaplib
import email


##################################################### code chung

# Thông tin Gmail
EMAIL_SENDER = "modpackphieuluu@gmail.com"
APP_PASSWORD = "gxqp sfjo ptem yyln"



# Hàm lưu email vào MySQL
def save_email(sender, receiver, subject, body):
    try:
        conn = dbconnect.connect_db()
        cursor = conn.cursor()

        # Kiem tra email da co trong DB chua
        if not is_email_exists(cursor, subject, sender):
            
            sql = "INSERT INTO emails (sender, receiver, subject, body) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (sender, receiver, subject, body))
            conn.commit()
            print("✅ Email đã lưu vào MySQL!")
        else:
            print("❌ Email này đã tồn tại trong cơ sở dữ liệu!")

        conn.close()
        

    except Exception as e:
        print(f"❌ Lỗi lưu email vào MySQL: {e}")

##################################################### Xử lý chức năng lưu mail đã gửi vào DB

# Hàm gửi email + lưu vào MySQL
def send_email(to_email, subject, body):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, APP_PASSWORD)

        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server.sendmail(EMAIL_SENDER, to_email, msg.as_string())
        server.quit()

        print("✅ Email đã gửi thành công!")

        # Lưu vào MySQL
        save_email(EMAIL_SENDER, to_email, subject, body)

    except Exception as e:
        print(f"❌ Lỗi gửi email: {e}")

# Gửi email test
# send_email("receiver_email@gmail.com", "Test Subject", "Nội dung email test")


##################################################### Xử lý chức năng lưu mail đã nhận vào DB

# hàm check email có lặp lại không? nếu có thì bỏ qua email đã có
def is_email_exists(cursor, subject, sender):
    sql = "SELECT COUNT(*) FROM emails WHERE subject = %s AND sender = %s"
    cursor.execute(sql, (subject, sender))
    return cursor.fetchone()[0] > 0

# Lấy nội dung email từ message
def extract_body(msg):
    """Lấy nội dung email từ đối tượng message"""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode()
    else:
        body = msg.get_payload(decode=True).decode()
    return body

# hàm nhận mail từ gmail và lưu vào MySQL
def fetch_emails():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(EMAIL_SENDER, APP_PASSWORD)
        mail.select("INBOX")

        result, email_data = mail.search(None, "ALL")
        email_ids = email_data[0].split()

        print(f"📩 Tìm thấy {len(email_ids)} email.")

        for email_id in email_ids[-5:]: # 5 mail mới nhất
            result, email_data = mail.fetch(email_id, "(RFC822)")
            raw_email = email_data[0][1]
            

            msg = email.message_from_bytes(raw_email)
            sender = msg["From"]
            subject = msg["Subject"]
            body = extract_body(msg)
            
            # Lưu email vào MySQL
            save_email(sender, EMAIL_SENDER, subject, body)

        mail.logout()
    except Exception as e:
        print(f"❌ Lỗi nhận email: {e}")

# Chạy thử nhận email
fetch_emails()