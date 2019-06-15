import socket
recv_ip="127.0.0.1"
recv_port=4444

# 0-1024 you can check free udp port netstat -nutlp
# Creating udp socket
# ip type v4,uDp

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Sending data to reciever

while True:
        data = input("Enter your message ")
        s.sendto(bytes(data,'utf-8'),(recv_ip,recv_port))
s.close()