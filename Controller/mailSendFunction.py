import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thông tin tài khoản gmail
EMAIL_SENDER = "modpackphieuluu@gmail.com"
PASSWORD_SENDER = "gxqp sfjo ptem yyln"

def send_email(to_email, subject, body):
    try:
        # kết nối Mail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        # server.ehlo() # Gửi lệnh EHLO để xác định với máy chủ
        server.starttls() # Mã hóa TLS
        server.login(EMAIL_SENDER, PASSWORD_SENDER)


        # Tạo mẫu email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Gửi email
        server.sendmail(EMAIL_SENDER, to_email, msg.as_string())
        server.quit()
        print("Email gửi thành công")
    except Exception as e:
        print(f"lỗi gửi email:{e}")
    
# Gửi email test
send_email("nguyenhuyilc2003@gmail.com", "Test Subject", "Nội dung email test")