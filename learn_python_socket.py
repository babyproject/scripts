import socket
import threading
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM )
sock.bind(("0,0,0,0", 9999))
sock.listen(1)
connections=[]

def handler(c, a):
    while True:
        data=c.recv(1024)
        c.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            print("disconnected..")
            break
while True:
    c, a=sock.accept()
    cthread=threading.Thread(target=handler, args=(c, a))
    cthread.daemon=True
    cthread.start()
    connections.append(c)
    print(connections)


