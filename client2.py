import socket
HOST=socket.gethostname()
PORT=123
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
data=client_socket.recv(1024)
print("Recieved message from server: ",data.decode())
client_socket.close()