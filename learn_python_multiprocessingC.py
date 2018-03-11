from multiprocessing import Process, connection, Queue
import sys

name="id1456"
address=("localhost", 10000)
def sendTo(args):
    conn=connection.Client(address, authkey="hello")
    conn.send(args)
    print("message out from {}".format(name))

def sendFrom(q):
    listener=connection.Listener(address, authkey="hello")
    while True:
        conn=listener.accept()
        data=conn.recv()
        if name in data[1]:
            print("message from {}:{}".format(data[0], data[2]))
            q.put(data)
            if data[2]=="quit":
                conn.close()

def core():
    global q
    q=Queue()
    p=Process(target=sendFrom, args=(q,))
    p.daemon=True
    p.start()
    p.join()
    while True:
        data=q.get()
        if data[2]=="quit":
            break
        else:
            print("i am still alive...{}".format(name))
            print("received: {}".format(data[2]))

core()
sys.exit(0)

