import socket
import threading
import time
import xml.dom.minidom as Dom
import re
import math
import sys

class communicate:
    def __init__(self):
        self.HOST, self.PORT = "localhost", 9999
        self.soc = socket.socket()
        self.soc.bind((self.HOST, self.PORT))
        self.soc.listen(10) #max number of clients listening to
        self.socket_list = []

    def AC_Req(self,Positive,Wind_Level):
        print("in req")
        print("AC_Req",Positive,Wind_Level)

    def parse(self,xml):
        root = Dom.parseString(xml).documentElement
        #print(root.nodeName)
        if(root.nodeName=='AC_Req'):
            node = root.getElementsByTagName('Positive')
            Positive = node[0].childNodes[0].data

            node = root.getElementsByTagName('Wind_Level')
            Wind_Level = node[0].childNodes[0].data
            
            self.AC_Req(Positive,Wind_Level)
    
    def recv(self,data,conn,addr):
        print("process:",data)
        data = data.decode()
        while(data):
            print("in recv")
            xml_len = int(re.findall('^[0-9]+',data)[0])
            head_len = int(math.log(xml_len,10))+1
            xml = data[head_len:head_len+xml_len]
            print("xml:",xml)
            self.parse(xml)
            data = data[1+head_len+xml_len:]
            print("data:",data)
        
    def broadcast(self,info):
        for (conn,addr) in self.socket_list:
            print("send:",info)
            try:
                conn.sendall(bytes(info,"utf-8"))
            except: #disconnected
                print("disconnected:",addr)
                self.socket_list.remove((conn,addr))

class receiver_thread(threading.Thread):
    def __init__(self,conn,addr):
        threading.Thread.__init__(self)
        print("init receiver:",addr)
        self.conn = conn
        self.addr = addr
        global server

    def run(self):
        print("Listen start")
        while(True):
            try:
                data = self.conn.recv(1024)
                print("data",data)
                server.recv(data,self.conn,self.addr)
            except:
                #print(sys.exc_info())
                pass
                   

class connector_thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global server

    def run(self):
        print("Listen start")
        while(True):
            conn, addr = server.soc.accept()
            conn.settimeout(10)
            print("connected:",conn,addr) #later this part should be moved to communicate.recv() when package is Login
            if (conn,addr) not in server.socket_list:
                server.socket_list.append((conn,addr))
                receiver_thread(conn,addr).start()
            
server = communicate()
connector_thread().start()
print('通信类已建立Server')
if __name__ == "__main__":
    while(1):
        time.sleep(5)
        server.broadcast("broadcast info")
