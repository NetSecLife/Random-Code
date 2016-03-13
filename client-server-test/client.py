'''
This script is just a way of learning about sockets and threading
There is no serious use for it
'''

import socket
import threading

HOST = "localhost"
PORT = 4444

def main():
    #Setup socket to send information
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Connecting to chat server at IP: " + str(HOST) + " and Port: " + str(PORT))
    s.connect((HOST, PORT))
    #Function to send
    def send():
        while True:
            msg = input("> ")
            s.send(msg.encode('utf-8'))
            reply = s.recv(1024)
            reply = reply.decode('utf-8')
            print(reply)

    while True:
        threading.Thread(target=send).start()
        break

if __name__ == '__main__':
    main()