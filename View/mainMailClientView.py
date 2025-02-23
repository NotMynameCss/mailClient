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
# gửi mail
import Controller.mailSendFunction as sendEmail
# xóa mail
import Controller.mailRemoveFunction as removeEmail
# search Mail
import Controller.mailSearchFunction as searchMail

class MainMailClientView:
    def __init__(self, email):
        self.email = email  # Email của người dùng đã đăng nhập
        self.root = tk.Tk()
        self.root.title(f"Mail Client - {self.email}")
        self.root.geometry("700x600")

        self.create_widgets()
        self.update_email_list()

        self.root.mainloop()
    def create_widgets(self):
        """Tạo giao diện chính của ứng dụng."""
        # Tiêu đề
        label = tk.Label(self.root, text=f"Hộp thư của {self.email}", font=("Arial", 14, "bold"))
        label.pack(pady=10)

        # Thanh tìm kiếm
        frame_search = tk.Frame(self.root)
        frame_search.pack(pady=5, fill="x", padx=10)

        self.entry_search = tk.Entry(frame_search, width=40)
        self.entry_search.pack(side="left", padx=5)

        search_button = tk.Button(frame_search, text="Tìm kiếm", command=self.search_email_ui)
        search_button.pack(side="left")

        # Bảng danh sách email
        self.tree = ttk.Treeview(self.root, columns=("ID", "Người gửi", "Chủ đề", "Thời gian"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Người gửi", text="Người gửi")
        self.tree.heading("Chủ đề", text="Chủ đề")
        self.tree.heading("Thời gian", text="Thời gian")
        self.tree.pack(expand=True, fill="both")
        
        # Gán sự kiện khi nhấp vào email
        self.tree.bind("<Double-1>", self.show_email_details)

        # Nút điều khiển
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(pady=10)

        delete_button = tk.Button(frame_buttons, text="Xóa Email", command=self.delete_email_ui, bg="red", fg="white", font=("Arial", 12))
        delete_button.pack(side="left", padx=10)

        refresh_button = tk.Button(frame_buttons, text="Làm mới", command=self.update_email_list)
        refresh_button.pack(side="left", padx=10)

        # Form gửi email
        frame_send = tk.Frame(self.root)
        frame_send.pack(pady=10, fill="x", padx=10)

        tk.Label(frame_send, text="Người nhận:", font=("Arial", 12)).pack(anchor="w")
        self.entry_receiver = tk.Entry(frame_send, width=50)
        self.entry_receiver.pack(pady=5)

        tk.Label(frame_send, text="Chủ đề:", font=("Arial", 12)).pack(anchor="w")
        self.entry_subject = tk.Entry(frame_send, width=50)
        self.entry_subject.pack(pady=5)

        tk.Label(frame_send, text="Nội dung:", font=("Arial", 12)).pack(anchor="w")
        self.text_body = tk.Text(frame_send, wrap="word", height=5, width=50)
        self.text_body.pack(pady=5)

        send_button = tk.Button(frame_send, text="Gửi Email", command=self.send_email_ui, bg="green", fg="white", font=("Arial", 12))
        send_button.pack(pady=5)

    #################################### chức năng hiển thị danh sách email
    # Cập nhật danh sách email vào bảng
    def update_email_list(self, emails=None):
        for row in self.tree.get_children():
            self.tree.delete(row)
        if emails is None:
            emails = fetchEmails.fetch_emails(self.email)
        for email in emails:
            self.tree.insert("", "end", values=email)
    #################################### chức năng đọc mail chi tiết
    # Hiển thị cửa sổ xem chi tiết email
    def show_email_details(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            email_id = item["values"][0]  # Lấy ID email được chọn
            details = readEmailDetail.fetch_email_details(email_id)

            if details:
                sender, receiver, subject, body, timestamp = details

                # Tạo cửa sổ chi tiết email
                detail_window = tk.Toplevel(self.root)
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

    #################################### chức năng gửi email từ giao diện
    # Gửi email từ giao diện
    def send_email_ui(self):
        to_email = self.entry_receiver.get()
        subject = self.entry_subject.get()
        body = self.text_body.get("1.0", tk.END)

        if not to_email or not subject or not body.strip():
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
            return

        sendEmail.send_email(to_email, subject, body)
        messagebox.showinfo("Thành công", "Email đã được gửi thành công!")

        # Xóa nội dung sau khi gửi
        self.entry_receiver.delete(0, tk.END)
        self.entry_subject.delete(0, tk.END)
        self.text_body.delete("1.0", tk.END)

        # Cập nhật danh sách email
        self.update_email_list()

    #################################### chức năng xóa email khi dùng nút xóa
    def delete_email_ui(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Lỗi", "Vui lòng chọn mail cần xóa!")
            return
        
        item = self.tree.item(selected_item)
        email_id = item["values"][0] # lấy ID email được chọn

        confirm = messagebox.askyesno("Thông báo Xác nhận", "Bạn có muốn xóa email này?")
        if confirm:
            removeEmail.delete_email(email_id)
            messagebox.showinfo("Thông báo Thành công", "Email đã được xóa!")
            self.update_email_list()



    ########################### chức năng search email
    # Xử lý tìm kiếm email
    def search_email_ui(self):
            keyword = self.entry_search.get()
            if not keyword:
                messagebox.showerror("Lỗi", "Vui lòng nhập từ khóa tìm kiếm!")
                return

            result = searchMail.search_emails(keyword)
            self.update_email_list(result)  # Hiển thị kết quả tìm kiếm

########################### Giao diện của main chương trình
def open_mainView(email):
    """Mở giao diện chính với mail đang dùng"""
    MainMailClientView(email)