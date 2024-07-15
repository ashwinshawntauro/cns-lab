import socket
HOST=socket.gethostname()
PORT=123
Message="Welcome"
print("Host name : ",HOST)
print("PORT: ",PORT)
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client_socket.sendto(Message.encode(),(HOST,PORT))

reply,addr=client_socket.recvfrom(1024)
print("Server: ",reply.decode())
reply_message="Thank you for connecting"

client_socket.sendto(reply_message.encode(),(HOST,PORT))
client_socket.close()
