import socket

sock = socket.socket()

try:
    sock.bind(('localhost', 80))
    print("Using port 80")
except OSError:
    sock.bind(('localhost', 8080))
    print("Using port 8080")

sock.listen(5)

conn, addr = sock.accept()
print("Connected", addr)

data = conn.recv(8192)
msg = data.decode().split()

print(msg)

resp = """HTTP/1.1 200 OK
Server: SelfMadeServer v0.0.1
Content-type: text/html
Connection: close

"""
filename = ''
if msg[1] == "/1":
    filename = '1.html'
elif msg[1] == "/2":
    filename = '2.html'
else:
    filename = 'index.html'

for line in open(filename).readlines():
    resp += line + '\n'

conn.send(resp.encode())

conn.close()