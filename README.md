# 🧪 socket-testbed-python

A modular TCP socket server/client testbed in Python with logging, configuration via YAML, and `pytest` testing support.

---

## 📁 Project Structure

```bash
socket-testbed-python/
├── socket_test/
│   ├── __init__.py
│   ├── client/
│   │   ├── __init__.py
│   │   ├── client_handler.py
│   │   └── __main__.py
│   ├── server/
│   │   ├── __init__.py
│   │   ├── server_handler.py
│   │   └── __main__.py
│   └── logger/
│       ├── __init__.py
│       └── logger.py
├── config/
│   ├── __init__.py
│   ├── client.yaml
│   └── server.yaml
├── tests/
│   ├── __init__.py
│   └── test_client_server.py
└── log/
    ├── client/
    └── server/
```

---

## 🚀 How to Run

### ✅ Run Server

```bash
python3 -m socket_test.server
```

### ✅ Run Client

```bash
python3 -m socket_test.client
```

> 💡 Logs are stored in `log/client/` and `log/server/` as JSON files with timestamped filenames.

---

## ⚙️ Configuration

Files are in `config` folder

Each contains:

```yaml
host: "127.0.0.1"
port: 5000
log_dir: "log/client"  # or "log/server"
```

You can edit ports and log folders here.

---

## 🧪 Testing with Pytest

Run the following from the project root:

```bash
pytest tests/
```

This will:

- Start the server in a background thread
- Run client communication test
- Assert the response contains the sent message

---

## 📦 Features

- Class-based TCP Client & Server
- Daily-rotated JSON log files
- Console + file logging (different formats)
- YAML-based configuration
- Structured project layout
- Pytest-based test suite

---

## 📌 Requirements

- Python 3.8+
- `pytest` (for tests)

Install via pip:

```bash
pip install -r requirements.txt
```
