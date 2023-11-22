import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
	server_socket.bind((socket.gethostname(), 56432))
	server_socket.listen(5)

while True:
	client_socket, address = server_socket.accept()
	print("Hello {} + {} ".format(client_socket, address))
	client_socket.send("Welcome to the server!", "utf-8")