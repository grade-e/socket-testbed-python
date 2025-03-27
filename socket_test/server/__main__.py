from socket_test.server.server_handler import TCPServer
from config import SERVER_HOST, SERVER_PORT, SERVER_LOG_FILE

def main():
    server = TCPServer(SERVER_HOST, SERVER_PORT, SERVER_LOG_FILE)
    server.run()

if __name__ == "__main__":
    main()