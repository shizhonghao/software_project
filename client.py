import socket
import sys
import time
import threading
import xml.dom.minidom as Dom

class communicate:
    def __init__(self):
        self.HOST, self.PORT = "localhost", 9999
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            # Connect to server and send data
        self.sock.connect((self.HOST, self.PORT))
        
    def send(self,info):
        data = info
        # Create a socket (SOCK_STREAM means a TCP socket)
        
        self.sock.sendall(bytes(data + "\n", "utf-8"))
        print("Sent:     {}".format(data))

    def AC_Req(self,Positive,Wind_Level):
        doc = Dom.Document() 
        root = doc.createElement("AC_Req")
        
        node_Pos = doc.createElement("Positive")
        node_Pos.appendChild(doc.createTextNode(str(Positive)))
        root.appendChild(node_Pos)
        
        node_Wind = doc.createElement("Wind_Level")
        node_Wind.appendChild(doc.createTextNode(str(Wind_Level)))
        root.appendChild(node_Wind)

        self.send(str(len(root.toxml())) + root.toxml())

    def recv(self,data):
        pass

class client_thread(threading.Thread):
    def __init__(self,client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        while(True):
            data = str(self.client.sock.recv(1024), "utf-8")
            print("Received: {}".format(data))
            self.client.recv(data)
            
c = communicate()
client_thread(c).start()
print('通信类已建立Client')

if __name__=="__main__":
    
    c.AC_Req(1,2)
    #c.AC_Req(1,3)
    i=1
    while(True):
        time.sleep(2)
        i = i + 1
        c.send(str(str(8) + "<t>" + str(i) + "<\t>"))
