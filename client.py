import socket
import sys
import time
import threading
import xml.dom.minidom as Dom
import re
import math
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtWidgets import QWidget

class communicate(QObject):
    _haslogged = pyqtSignal(int,str,str,int)
    wind_change_ac = pyqtSignal(int,int)
    temp_freq_change = pyqtSignal(int)
    fare_info_change = pyqtSignal(float,float)

    def __init__(self):
        super().__init__()
        print("client")
        #super(QWidget,self).__init__()
        print("client init")
        self.HOST, self.PORT = "192.168.43.234", 9999#"localhost",9999 #
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Connect to server and send data
        self.sock.connect((self.HOST, self.PORT))

    def AC_Req(self,Positive,Wind_Level):
        doc = Dom.Document() 
        root = doc.createElement("AC_Req")
        
        node_Pos = doc.createElement("Positive")
        node_Pos.appendChild(doc.createTextNode(str(Positive)))
        root.appendChild(node_Pos)
        
        node_Wind = doc.createElement("Wind_Level")
        node_Wind.appendChild(doc.createTextNode(str(Wind_Level)))
        root.appendChild(node_Wind)

        self.send(root.toxml() + '\n')

    def Temp_Submit(self,Time,Client_No,Temp):
        doc = Dom.Document()
        root = doc.createElement("Temp_Submit")

        node_Time = doc.createElement("Time")
        node_Time.appendChild(doc.createTextNode(str(Time)))
        root.appendChild(node_Time)

        node_CNO = doc.createElement("Client_No")
        node_CNO.appendChild(doc.createTextNode(str(Client_No)))
        root.appendChild(node_CNO)

        node_Temp = doc.createElement("Temp")
        node_Temp.appendChild(doc.createTextNode(str(Temp)))
        root.appendChild(node_Temp)

        self.send(root.toxml() + '\n')

    def Login(self,Name,Password,Client_No):
        self.Temp_Submit(1,Client_No,25)
        #self._haslogged.emit(1,Name, Password, 1)
        doc = Dom.Document()
        root = doc.createElement("Login")

        node_Name = doc.createElement("Name")
        node_Name.appendChild(doc.createTextNode(str(Name)))
        root.appendChild(node_Name)

        node_Pass = doc.createElement("Password")
        node_Pass.appendChild(doc.createTextNode(str(Password)))
        root.appendChild(node_Pass)

        node_CNO = doc.createElement("Client_No")
        node_CNO.appendChild(doc.createTextNode(str(Client_No)))
        root.appendChild(node_CNO)

        self.send(root.toxml() + '\n')

    # ------local setting functions
    def Login_ACK(self,Succeed,Name,Password,Mode):
        self._haslogged.emit(int(Succeed),Name,Password,int(Mode))

    def Mode(self,Heater):
        pass

    def Wind(self,Level,Start_Blowing):
        self.wind_change_ac.emit(int(Level),int(Start_Blowing))
        pass

    def Fare_Info(self,Fare,Energy):
        self.fare_info_change.emit(float(Fare),float(Energy))
        pass

    def Temp_Submit_Freq(self,Temp_Submit_Freq):
        self.temp_freq_change.emit(int(Temp_Submit_Freq))
        pass

    # ------info processing functions
    def parse(self,xml):
        print("parse xml:",xml)
        root = Dom.parseString(xml).documentElement

        if (root.nodeName == "Login_ACK"):
            node = root.getElementsByTagName("Succeed")
            Succeed = node[0].childNodes[0].data

            node = root.getElementsByTagName("Name")
            Name = node[0].childNodes[0].data

            node = root.getElementsByTagName("Password")
            Password = node[0].childNodes[0].data

            node = root.getElementsByTagName("Mode")
            Mode = node[0].childNodes[0].data

            self.Login_ACK(Succeed,Name,Password,Mode)

        if (root.nodeName == "Mode"):
            node = root.getElementsByTagName("Heater")
            Heater = node[0].childNodes[0].data

            #self.Login_ACK(Heater)

        if (root.nodeName == "Wind"):
            node = root.getElementsByTagName("Level")
            Level = node[0].childNodes[0].data

            node = root.getElementsByTagName("Start_Blowing")
            Start_Blowing = node[0].childNodes[0].data

            self.Wind(Level,Start_Blowing)

        if (root.nodeName == "Fare_Info"):
            node = root.getElementsByTagName("Fare")
            Fare = node[0].childNodes[0].data

            node = root.getElementsByTagName("Energy")
            Energy = node[0].childNodes[0].data

            self.Fare_Info(Fare,Energy)

        if (root.nodeName == "Temp_Submit_Freq"):
            node = root.getElementsByTagName("Temp_Submit_Freq")
            Temp_Submit_Freq = node[0].childNodes[0].data

            self.Temp_Submit_Freq(Temp_Submit_Freq)

    def recv(self,data,soc):
        print("process:", data,len(data))
        data = data.decode()
        while (data):
            print("in recv")
            if(len(data)<4):
                data = data + str(soc.recv(1024), "utf-8")
                print(len(data))
            d_len = bytearray(data[0:4].encode('ascii'))
            print(d_len[0],d_len[1],d_len[2],d_len[3])
            xml_len = d_len[3] + (d_len[2]<<8) + (d_len[1]<<16) + (d_len[0]<<24)
            print("xml_len:",xml_len)
            data = data[4:]
            #int(re.findall('^[0-9]+', data)[0])
            #head_len = int(math.log(xml_len, 10)) + 1
            if(len(data) < xml_len):
                data = data + str(soc.recv(1024), "utf-8")
            xml = data[:xml_len]
            data = data[xml_len:]
                #data[head_len:head_len + xml_len]
            print("xml:", xml)
            self.parse(xml)
            print("data:", data)

    def send(self, info):
        self.sock.sendall(len(info).to_bytes(4,'big') + bytes(info, "utf-8"))
        print("Sent:     {}".format(info))


class client_thread(threading.Thread):
    def __init__(self,client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        while(True):
            data = self.client.sock.recv(1024)
            print("Received: {}".format(data))
            self.client.recv(data,self.client.sock)
            
c = communicate()
client_thread(c).start()
print('通信类已建立Client')

if __name__=="__main__":
    
    c.AC_Req(1,2)
    c.Login("frank","123456789",103)
    i=1
    while(True):
        time.sleep(7)
        i = i + 1
        c.send(str(str(8) + "<t>" + str(i) + "<\t>"))
