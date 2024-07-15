import socket
HOST=socket.gethostname()
PORT=123

print("Host name: ",HOST)
print("Port: ",PORT)
print("IP address: ",socket.gethostbyname(HOST))
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((HOST,PORT))
while True:
    data, addr =server_socket.recvfrom(1024)
    print("Message Recieved: ",data.decode())
    print("From: ",addr)
    reply_message="Thanks for the Message!"
    server_socket.sendto(reply_message.encode(),addr)
    data2,addr2=server_socket.recvfrom(1024)
    print("Message Recieved: ",data2.decode())
    print("From: ",addr2)
