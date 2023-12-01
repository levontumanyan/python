import socket
import threading

PORT = 56232

# receive messages function
def receive_messages(message):
	while True:
		data = client_socket.recv(1024).decode('utf-8')
		if data.lower() == 'exit':
			print("Server has shut down. Goodbye!")
			client_socket.close()
			break
		print(data)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#client_socket.connect((socket.gethostname(), 56232))
client_socket.connect(('127.0.0.1', PORT))

client_socket.recv(1024).decode('utf-8')

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

	# if (message.lower() == "quit"):
	# 	print("Exiting the chat...")
	# 	client_socket.close()
	# 	close_thread=True
	# 	break

	client_socket.send(message.encode('utf-8'))
