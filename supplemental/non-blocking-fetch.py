import socket


sock = socket.socket()
sock.setblocking(False)
try:
    sock.connect(('127.0.0.1', 8000))
except BlockingIOError:
    pass

request = 'GET /blog/ HTTP/1.0\r\nHost: www.myblog.com\r\n\r\n'
encoded = request.encode('ascii')
while True:
    try:
        sock.send(encoded)
        break
    except OSError as e:
        pass

print('sent')