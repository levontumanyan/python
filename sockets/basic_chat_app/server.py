import socket
import threading
import signal
import sys

PORT = 56232

def handle_client(client_socket):

	# todo: client_socket.send("Welcome to the chat my boy".encode('utf-8'))
	try:
		client_socket.send("Welcome to the chat my boy".encode('utf-8'))
		username = client_socket.recv(1024).decode('utf-8')
		broadcast(('{} has entered the chat...There are {} users in the chat'.format(username, len(clients))), client_socket)
		
		while True:
		
			data = client_socket.recv(1024).decode('utf-8')

			if not data:
				break
			
			broadcast(('{}: {} '.format(username, data)), client_socket)
	except Exception as e:
		print(f"Error handling client: {e}")
	finally:
		client_socket.close()

def broadcast(message, client_to_send):
	for client in clients:
		try:
			if (client != client_to_send):
				client.send(message.encode('utf-8'))
		except:
			clients.remove(client)

# configure the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', PORT))
server_socket.listen(10)

# signal handler function
def signal_handler(sig, frame):
	# disconnect clients
	
	# for client in clients:
	# 	broadcast(("Terminating the session from the server side..."), client)
	# 	client.close()

	for client in clients:
		try:
			client.send('exit'.encode('utf-8'))
			client.close()
		except:
			pass  # Handle exceptions as needed

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