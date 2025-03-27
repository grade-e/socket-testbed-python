import socket
import time
from socket_test.logger.logger import get_logger

class TCPClient:
    def __init__(self, host, port, log_file):
        self.host = host
        self.port = port
        self.logger = get_logger("TCPClient", log_file)
        self.sock = None

    def connect(self):
        while True:
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((self.host, self.port))
                self.logger.info("Connected to server.")
                break
            except ConnectionRefusedError:
                self.logger.warning("Connection failed. Retrying in 1 second...")
                time.sleep(1)

    def run(self):
        self.connect()
        with self.sock:
            while True:
                msg = input("Enter message (type 'exit' to quit): ")
                if msg.lower() == 'exit':
                    break
                self.logger.debug(f"Sending: {msg}")
                self.sock.sendall(msg.encode())
                data = self.sock.recv(1024)
                self.logger.info(f"Server replied: {data.decode()}")
