## khắc phục lỗi đường dẫn, đảm bảo đường dẫn chính xác
import sys
import os
# Thêm thư mục gốc của dự án vào sys.path: sử dụng để đường dẫn chính xác
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# giao diện
import tkinter as tk
from tkinter import ttk, messagebox
# đọc chi tiết email
import Controller.mailReadDetailFunction as readEmailDetail
# hiển thị danh sách email
import Controller.mailFetchFunction as fetchEmails




#################################### chức năng đọc mail chi tiết
# Hiển thị cửa sổ xem chi tiết email
def show_email_details(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        email_id = item["values"][0]  # Lấy ID email được chọn
        details = readEmailDetail.fetch_email_details(email_id)

        if details:
            sender, receiver, subject, body, timestamp = details

            # Tạo cửa sổ chi tiết email
            detail_window = tk.Toplevel(root)
            detail_window.title(f"Chi tiết Email - {subject}")
            detail_window.geometry("500x400")

            tk.Label(detail_window, text=f"Người gửi: {sender}", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
            tk.Label(detail_window, text=f"Người nhận: {receiver}", font=("Arial", 12)).pack(anchor="w", padx=10)
            tk.Label(detail_window, text=f"Thời gian: {timestamp}", font=("Arial", 10, "italic")).pack(anchor="w", padx=10, pady=5)
            tk.Label(detail_window, text="Nội dung:", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)

            text_body = tk.Text(detail_window, wrap="word", height=10, width=50)
            text_body.insert("1.0", body)
            text_body.config(state="disabled")  # Không cho chỉnh sửa
            text_body.pack(padx=10, pady=5, fill="both", expand=True)


#################################### chức năng hiển thị danh sách email


# Cập nhật danh sách email vào bảng
def update_email_list():
    for row in tree.get_children():
        tree.delete(row)
    emails = fetchEmails.fetch_emails()
    for email in emails:
        tree.insert("", "end", values=email)

# Giao diện Tkinter
root = tk.Tk()
root.title("Mail Client - Danh sách Email")
root.geometry("600x400")

# Tiêu đề
label = tk.Label(root, text="Danh sách Email", font=("Arial", 14))
label.pack(pady=10)

# Tạo bảng danh sách email
columns = ("ID", "Người gửi", "Chủ đề", "Thời gian")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Người gửi", text="Người gửi")
tree.heading("Chủ đề", text="Chủ đề")
tree.heading("Thời gian", text="Thời gian")
tree.pack(expand=True, fill="both")

# thêm sự kiện nhấp vào để đọc mail chi tiết
tree.bind("<Double-1>", show_email_details)

# Nút làm mới danh sách
refresh_button = tk.Button(root, text="Làm mới", command=update_email_list)
refresh_button.pack(pady=10)



######################## Hiển thị danh sách email khi mở chương trình
update_email_list()


######################## Chạy giao diện
root.mainloop()
