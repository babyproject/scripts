from multiprocessing import Process, connection, Queue
import sys
import time

name="id5676"
address=("localhost", 10001)
def sendTo(args):
    conn=connection.Client(address, authkey="hello")
    conn.send(args)

def sendFrom(q):
    listener=connection.Listener(("localhost", 10000), authkey="hello")
    while True:
        conn=listener.accept()
        data=conn.recv()
        q.put(data)


def core():
    q=Queue()
    p=Process(target=sendFrom, args=(q,))
    p.daemon=True
    p.start()
    #p.join()

    while True:
        if q.empty():
            d=raw_input("enter anything:")
            sendTo([name, ["id5676", "id3245"], d])
            if d=="quit":
                break
        else:
            data=q.get()
            if name in data[1]:
                if data[2]=="quit":
                    break
                else:
                    print("received from {}: {}".format(data[0], data[2]))

core()
sys.exit(0)
