
# SERVER , ACTS AS AN INTERFACE BETWEEN TWO USERS

import socket
s = socket.socket()
print(' SOCKET CREATED ')
s.bind(('localhost', 9999))
flag = True
cls = ''
s.listen(2)
print(' WAITING FOR CLIENT CONNECTIONS ')
while flag:

    c, add1 = s.accept()
    d, add2 = s.accept()
    print(' CONNECTED WITH {} '.format(add1))
    print(' CONNECTED WITH {} '.format(add2))

    while flag:
        cls = c.recv(1024).decode()
        if cls == 'None':
            d.send(bytes('None', 'utf-8'))
            flag = False
        else:
            d.send(bytes(cls, 'utf-8'))

    c.close()
    d.close()
