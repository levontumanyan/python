import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((socket.gethostname(), 56432))

while True:
	client_message = input("What would you like to send to the server: ")

	client_socket.send(client_message.encode("ascii"))

	data = client_socket.recv(1024)

	client_socket.close()

	print('Received', repr(data))