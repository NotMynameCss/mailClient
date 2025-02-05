################################ khắc phục lỗi đường dẫn, đảm bảo đường dẫn chính xác
import sys
import os
# Thêm thư mục gốc của dự án vào sys.path: sử dụng để đường dẫn chính xác
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

################################ giao diện
import tkinter as tk
from tkinter import ttk
################################ cơ sở dữ liệu
import Model.dbConnector as dbconnect

# Hàm lấy danh sách email từ MySQL
def fetch_emails():
    conn = dbconnect.connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, sender, subject, timestamp FROM emails ORDER BY timestamp DESC")
    emails = cursor.fetchall()
    conn.close()
    return emails

# Cập nhật danh sách email vào bảng
def update_email_list():
    for row in tree.get_children():
        tree.delete(row)
    emails = fetch_emails()
    for email in emails:
        tree.insert("", "end", values=email)

# Giao diện Tkinter
root = tk.Tk()
root.title("Mail Client - Danh sách Email")
root.geometry("600x400")

# Tiêu đề
label = tk.Label(root, text="Danh sách Email", font=("Arial", 14))
label.pack(pady=10)

# Tạo bảng hiển thị email
columns = ("ID", "Người gửi", "Chủ đề", "Thời gian")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Người gửi", text="Người gửi")
tree.heading("Chủ đề", text="Chủ đề")
tree.heading("Thời gian", text="Thời gian")
tree.pack(expand=True, fill="both")

# Nút làm mới danh sách
refresh_button = tk.Button(root, text="Làm mới", command=update_email_list)
refresh_button.pack(pady=10)

# Hiển thị danh sách email khi mở chương trình
update_email_list()

# Chạy giao diện
root.mainloop()
