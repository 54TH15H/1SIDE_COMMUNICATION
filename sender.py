
import socket
c = socket.socket()
c.connect(('localhost', 9999))
flag = True

while flag:
    print(' PRESS 1 TO STOP: ')
    x = input()

    if x == '1':
        c.send(bytes('None', 'utf-8'))
        flag = False
    else:
        c.send(bytes(x, 'utf-8'))

