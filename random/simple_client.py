import socket

HOST = '192.168.0.164'
PORT = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
server.sendall(('Hello'.encode()))
server.close()