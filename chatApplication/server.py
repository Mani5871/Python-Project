import socket

port = 3000
host_name = '127.0.0.1'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host_name, port))
print(f"Server is live on {s.getsockname()}")
