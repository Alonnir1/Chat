import socket
from dotenv import load_dotenv
import os

load_dotenv()  

HOST = os.getenv("CLIENT_HOST")
PORT = int(os.getenv("PORT"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, server!")
    data = s.recv(1024)

print("Received from server:", data.decode())
