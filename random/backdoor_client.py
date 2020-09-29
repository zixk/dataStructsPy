import socket

HOST = '192.168.0.164'
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
    message = input("\n-Select an option: ")

    if(message == "0"):
        s.sendall(message.encode())
        s.close()
        break
    elif(message == "1"):
        s.sendall(message.encode())
        data = s.recv(1024)
        if not data: break
        print(data.decode('utf-8'))
    elif(message == "2"):
        path = input("Insert the path: ")
        s.sendall(message.encode())
        s.sendall(path.encode())
        data = s.recv(1024)
        data = data.decode('utf-8').split(",")
        print("*"*40)
        for x in data:
            print(x)
        print("*"*40)