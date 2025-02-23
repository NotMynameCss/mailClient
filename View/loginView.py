# (Giao diện đăng nhập)
# khắc phục đường dẫn không chính xác
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# giao diện
import tkinter as tk
from tkinter import messagebox
# xử lý đăng nhập
import Controller.authFunction as auth
import View.mainMailClientView as mainView


def login():
    email = entry_email.get()
    password = entry_password.get()

    if not email or not password:
        messagebox.showerror("Lỗi", "Vui lòng nhập email và mật khẩu!")
        return

    if auth.login_gmail(email, password):
        messagebox.showinfo("Thành công", "Đăng nhập thành công!")
        root.destroy()  # Đóng cửa sổ đăng nhập
        # TODO: Chuyển sang màn hình chính của chương trình
        mainView.open_mainView(email)
    else:
        messagebox.showerror("Lỗi", "Email hoặc mật khẩu không đúng!")

# Tạo cửa sổ đăng nhập
root = tk.Tk()
root.title("Đăng nhập Mail Client")
root.geometry("300x200")

tk.Label(root, text="Email:", font=("Arial", 12)).pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack(pady=5)

tk.Label(root, text="Mật khẩu:", font=("Arial", 12)).pack(pady=5)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack(pady=5)

btn_login = tk.Button(root, text="Đăng nhập", command=login)
btn_login.pack(pady=10)

root.mainloop()
