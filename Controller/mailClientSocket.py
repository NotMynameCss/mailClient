import socket

class MailClientSocket:
    def __init__(self, host="127.0.0.1", port=5050):
        """Kết nối đến Mail Server TCP"""
        self.server_host = host
        self.server_port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.server_host, self.server_port))

    def send_request(self, request):
        """Gửi yêu cầu đến server và nhận phản hồi"""
        try:
            self.client.sendall(request.encode("utf-8"))
            response = self.client.recv(4096).decode("utf-8")
            return response
        except Exception as e:
            print(f"Lỗi kết nối đến server: {e}")
            return None

    def close(self):
        """Đóng kết nối với server"""
        self.client.close()
