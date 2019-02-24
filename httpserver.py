import socket
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# simple version
#
# class MyHTTPserver(BaseHTTPRequestHandler):
#     def do_GET(self):
#         print(self.path)
#         enc = "UTF-8"
#         self.protocol_version = "HTTP/1.1"
#         self.send_response(200)
#         self.send_header("Content-type","text/html; charset=%s" %enc)
#         f = open("baidu.html","r",encoding="utf-8")
#         strs = f.read()
#         self.send_header("Content-Lenth",str(len(strs)))
#         self.end_headers()
#         self.wfile.write(bytes(strs,encoding="UTF-8"))
#
#
# httpd = HTTPServer(('',8080),MyHTTPserver)
# print("SERVER:8080")
# httpd.serve_forever()


def Do_GET(sock,html):
    f = open("baidu.html","r",encoding="utf-8")
    strs = f.read()
    send_message = "HTTP/1.1 200 OK\r\n" \
                    "Connection: close\r\n" \
                   "Content-type: text/html\r\nContent-Lenth:"\
                   + str(len(strs)) + "\r\n\r\n"\
                   + strs
    print(send_message)
    sock.send(bytes(send_message,encoding="utf-8"))


def link(sock,addr):
    print("Accept %s:%s's connection" %addr)
    buffer = []
    while True:
        buf = sock.recv(1024)
        if buf:
            buffer.append(buf)
        else:
            break;
    data = b"".join(buffer)
    header,html = data.split(b"\r\n\r\n",1)
    Method,trash = data.split(b" / ",1)
    Method = Method.decode(encoding="utf-8")
    if Method == "GET":
        Do_GET(sock,html)
    elif Method == "POST":
        print("b")

Local = ("127.0.0.1",8080)
LocalSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LocalSocket.bind(Local)
LocalSocket.listen(5)
print("listen 8080")

while True:
    sock,addr = LocalSocket.accept()
    task = threading.Thread(target = link,args = (sock,addr))
    task.start()

