import socket
HOST=socket.gethostname()
PORT=123
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))
actual_port=server_socket.getsockname()[1]
server_socket.listen(5)
print("Server is running on: ")
print("HOST: ",HOST)
print("PORT: ",actual_port)
print("IP Address: ",socket.gethostbyname(HOST))
while True:
    client_socket,client_address=server_socket.accept()
    print(f"Connection form {client_address[0]}:{client_address[1]} has been established")
    client_socket.sendall(b"Thanks for connecting")
    client_socket.close()