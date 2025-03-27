import socket
from socket_test.logger.logger import get_logger

class TCPServer:
    def __init__(self, host, port, log_file):
        self.host = host
        self.port = port
        self.logger = get_logger("TCPServer", log_file)

    def handle_client(self, conn, addr):
        self.logger.info(f"Connected: {addr}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    self.logger.info(f"Client {addr} disconnected.")
                    break
                self.logger.debug(f"Raw data: {data}")
                self.logger.info(f"Received: {data.decode()}")
                response = f"Server received: {data.decode()}"
                conn.sendall(response.encode())

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_sock.bind((self.host, self.port))
            server_sock.listen()
            self.logger.info(f"Listening on {self.host}:{self.port}...")

            while True:
                try:
                    conn, addr = server_sock.accept()
                    self.handle_client(conn, addr)
                except Exception as e:
                    self.logger.error(f"Error: {e}")