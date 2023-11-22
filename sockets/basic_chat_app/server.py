import socket
import threading
import signal
import sys

def handle_client(client_socket):

	username = client_socket.recv(1024).decode('utf-8')

	while True:	
	
		data = client_socket.recv(1024).decode('utf-8')

		if not data:
			break
		
		broadcast(('{}: {} '.format(username, data)), client_socket)
	client_socket.close()

def broadcast(message, sender_client):
	for client in clients:
		try:
			if (client != sender_client):
				#message = '{0}: {1}'.format(client.getsockname(), message)
				client.send(message.encode('utf-8'))
		except:
			clients.remove(client)

# configure the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server_socket.bind((socket.gethostname(), 56232))
server_socket.bind(('0.0.0.0', 56232))
server_socket.listen(10)

def signal_handler(sig, frame):
    print("\nClosing the server...")
    server_socket.close()
    sys.exit(0)

# Set up signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

print("Server listening for connections...")

# List to store connected clients
clients = []

while True:
	client_socket, addr = server_socket.accept()

	print('Server accepted a connection from {}'.format(addr))

	# add the new client to the list
	clients.append(client_socket)

	# Start a new thread to handle the client
	client_handler = threading.Thread(target=handle_client, args=(client_socket,))
	client_handler.start()