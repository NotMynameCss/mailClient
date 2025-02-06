# Thêm thư mục gốc của dự án vào sys.path: sử dụng để đường dẫn chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Controller
import Controller.mailReadDetailFunction as readDetailFunction
# giao diện
import tkinter as tk
from tkinter import ttk

# Hiển thị cửa sổ xem chi tiết email
def show_email_details(event):
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        email_id = item["values"][0]  # Lấy ID email được chọn
        details = readDetailFunction.fetch_email_details(email_id)

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


