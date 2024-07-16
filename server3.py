import socket
UDP_HOST=socket.gethostname()
UDP_PORT=5005  
print("UDP Host: ",UDP_HOST)
print("UDP Port: ",UDP_PORT)
print("IP Address: ",socket.gethostbyname(UDP_HOST))
server_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_socket.bind((UDP_HOST,UDP_PORT))
while True:
    data,addr=server_socket.recvfrom(1024)
    print("Client: ",data.decode())
    server_socket.sendto(b"Thanks for the message",addr)
    data2,addr2=server_socket.recvfrom(1024)
    print("Client: ",data2.decode())
    # server_socket.close()