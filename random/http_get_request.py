import http.client

print("** This program returns verifies if a specific resource exists **\n")

HOST = '195.114.1.10'
PORT = 80
url = input("Insert the url: ")
try:
    connection = http.client.HTTPConnection(HOST, PORT)
    connection.request('GET', url)
    response = connection.getresponse()
    print("Server response:", response.status)
    connection.close()
except ConnectionRefusedError:
    print("Connection failed")