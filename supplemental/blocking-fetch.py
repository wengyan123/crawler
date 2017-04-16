import socket


def threaded_method():
    sock = socket.socket()
    sock.connect(('127.0.0.1', 8000))
    request = 'GET /blog/ HTTP/1.0\r\nHost: www.google.com\r\n\r\n'
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    print(response)

threaded_method()
