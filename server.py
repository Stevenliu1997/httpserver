import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STTREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('waiting for connection...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock,addr))
    t,start()

    def tcplink(sock,addr):
        print('Accept new connectionfrom %s:%s...' %addr)
        sock.send(b'Welcome!')
        while True:
            data