import socket
UDP_HOST=socket.gethostname()
UDP_PORT=5005
Message="Welcome to CNS"

print("UDP Host: ",UDP_HOST)
print("UDP Port: ",UDP_PORT)
print("Message: ",Message)

client_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_server.sendto(Message.encode(),(UDP_HOST,UDP_PORT))
reply,addr=client_server.recvfrom(1024)
print("Server: ",reply.decode())
reply_mess="Thank you for connecting!"
client_server.sendto(reply_mess.encode(),(UDP_HOST,UDP_PORT))
client_server.close()
