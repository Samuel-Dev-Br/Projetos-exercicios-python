import socket

ports = [80]

for port in ports:
    cliente = socket.socket(socket._AFINNET, socket.SOCK.STREAM)
    cliente.settimeout(0.1)
    code = cliente.connect_ex(('127.0.0.1' ,port))
    if code == 0:
        print(ports, "OPEN")







