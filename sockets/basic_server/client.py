import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((socket.gethostname, 56432))

client_socket.send(b'Hello World!')

data = client_socket.recv(1024)

client_socket.close()

print('Received', repr(data))