import http.client

print("** This program returns a list of methods if OPTIONS is enabled **\n")

HOST = '195.114.1.10'
PORT = 80

if(PORT == ""):
    PORT = 80

try:
    connection = http.client.HTTPConnection(HOST, PORT)
    connection.request('OPTIONS', '/')
    response = connection.getresponse()
    print("Enabled methods are: ", response.getheader('allow'))
    connection.close()
except ConnectionRefusedError:
    print("Connection failed")