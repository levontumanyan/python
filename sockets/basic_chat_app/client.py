import socket
import threading

# receive messages function
def receive_messages(message):
	while True:
		data = client_socket.recv(1024).decode('utf-8')
		print(data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client_socket.connect((socket.gethostname(), 56232))
client_socket.connect(('127.0.0.1', 56232))

# get the username
username = input("Please enter your username: ")
# send the username to the server
client_socket.send(username.encode('utf-8'))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

# Main loop to send messages:
while True:
	message = input()

	client_socket.send(message.encode('utf-8'))