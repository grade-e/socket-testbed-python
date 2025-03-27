from socket_test.client.client_handler import TCPClient
from config import CLIENT_HOST, CLIENT_PORT, CLIENT_LOG_FILE

if __name__ == "__main__":
    client = TCPClient(CLIENT_HOST, CLIENT_PORT, CLIENT_LOG_FILE)
    client.run()
