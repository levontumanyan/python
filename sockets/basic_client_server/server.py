import socket

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
# 	server_socket.bind((socket.gethostname(), 56432))
# 	server_socket.listen(5)

# 	client_socket, address = server_socket.accept()
# 	print("Hello {} + {} ".format(client_socket, address))
# 	client_socket.send("Welcome to the server!", "utf-8")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((socket.gethostname(), 56432))

server_socket.listen(5)

while True:
	client_socket, addr = server_socket.accept()

	print('Got a connection from {}'.format(client_socket))
	print('Address:{}'.format(addr))

	msg = 'Hello client how is it going'
	client_socket.send(msg.encode('ascii'))

	data = server_socket.recv(1024)

	print('Received', repr(data))

	client_socket.close()
