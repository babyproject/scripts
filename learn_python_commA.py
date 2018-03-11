import os
import pickle
import types
import shutil
import time
import multiprocessing as mtp

packageSample={"mode":"join", "from":"id123", "to":["id234", "id789"], "time":"20181012122123","type":"unknown", "tag":["dog", "white"], "dataSet":"image object"}

class cellComm(object):
    def __init__(self):
        self.package="package.pkl"
        self.pklTemp="temp.pkl"
        self.commScript="comm.py"
        self.cellScript="cell.py"
        self.database="cell.db"
        self.cwdir=os.path.dirname(__file__)
        self.pwdir=os.path.dirname(self.cwdir)

    #check if any file received to awake cell
    def listen(self):
        if os.path.exists(self.package):
            pfile=open(self.package, "rb")
            data=pickle.load(pfile)
            pfile.close()
            if type(data)==dict:
                self.awakeCell()
            os.remove(self.package)

    #return data passed on
    def recv(self):
        if os.path.exists(self.package):
            pfile=open(self.package, "rb")
            self.data=pickle.load(pfile)
            pfile.close()
            if type(self.data)==dict:
                return self.data
            else:
                os.remove(self.package)
                return False

    #send() function accepts packaged dictionary object 
    def send(self, packageObject):
        self.packageObject=packageObject
        if type(self.packageObject)==dict:
            temp=open(self.pklTemp, "wb")
            pickle.dump(self.packageObject, temp)
            temp.close()
            for item in self.packageObject["to"]:
                shutil.copy(self.pklTemp, (item+r"/"+self.package))
                self.awakeComm(item+r"/"+self.commScript)
            os.remove(self.pklTemp)

    #awake "comm.py" of target cell to activate communication
    def awakeComm(self, desObject):
        p=mtp.Process(target=execfile(desObject))
        p.daemon=False
        p.start()
    
    #awake "cell.py" of target cell to activate it's body
    def awakeCell(self):
        p=mtp.Process(target=execfile(self.cellScript))
        p.daemon=False
        p.start()

    def run(self):
        self.listen()
