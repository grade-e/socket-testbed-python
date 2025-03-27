import yaml
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)

with open(os.path.join(BASE_DIR, "client.yaml"), "r") as f:
    client_config = yaml.safe_load(f)

with open(os.path.join(BASE_DIR, "server.yaml"), "r") as f:
    server_config = yaml.safe_load(f)

# 공통 시간 포맷으로 로그 이름 지정
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# 클라이언트 설정
CLIENT_HOST = client_config.get("host", "127.0.0.1")
CLIENT_PORT = client_config.get("port", 5000)
CLIENT_LOG_DIR = client_config.get("log_dir", "log/client")
CLIENT_LOG_FILE = os.path.join(CLIENT_LOG_DIR, f"client_{timestamp}.json")

# 서버 설정
SERVER_HOST = server_config.get("host", "127.0.0.1")
SERVER_PORT = server_config.get("port", 5000)
SERVER_LOG_DIR = server_config.get("log_dir", "log/server")
SERVER_LOG_FILE = os.path.join(SERVER_LOG_DIR, f"server_{timestamp}.json")