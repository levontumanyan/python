import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)

print(socket.__builtins__)

print(host_name)
print(ip_address)
