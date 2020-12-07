
import socket
d = socket.socket()
d.connect(('localhost',9999))
flag = True

while flag:

    x = d.recv(1024).decode()
    if x == 'None':
        flag = False
    else:
        print(x)

