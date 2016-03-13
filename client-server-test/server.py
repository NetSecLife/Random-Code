'''
This script is just a way of learning about sockets and threading
There is no serious use for it
'''

import socket
import threading

HOST = "localhost"
PORT = 4444

def main():
    #Setup the socket to accept incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    print("Socket created on Port: " + str(PORT))
    conn, addr = s.accept()
    print("Conenction Incoming: " + str(addr))
    #Function to recv
    def recv():
        while True:
            try:
                data = conn.recv(1024)
            except:
                print("Connection Closed.")
                break
            if not data: break
            if data:
                msg = data.decode('utf-8')
                print(str(addr[0]) + " > " + msg)
                reply = "RECV..." + msg
                conn.send(reply.encode('utf-8'))

    while True:
        threading.Thread(target=recv).start()
        break


if __name__ == '__main__':
    main()