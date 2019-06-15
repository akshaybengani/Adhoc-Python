import socket
recv_ip="127.0.0.1"
recv_port=4444
# 0-1024 you can check free udp port netstat -nutlp
# Creating udp socket
# ip type v4,uDp

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# fitting ip and port with UDP socket
s.bind((recv_ip,recv_port))

# recieving data from sender
while True:
        data = s.recvfrom(256)
        print(data[0])

s.close()