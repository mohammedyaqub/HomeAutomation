import socket
import random
import time
import pickle


host=socket.gethostbyname(socket.gethostname())#to know the host name
port=1124
port1=5325

s_B=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#to create socket
s_B.bind((host,port))#assign ip address and port number to socket
s_B.listen(5)#listen to incoming connections
s_A1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to create socket
s_A1.connect((host, port1))
c_C, adr=s_B.accept()#




#for sending random data from slave to master
def sendingData(data):
    c_C.send(data)#clt.send(bytes(st,'utf-8'))for sending data

while True:
    data=s_A1.recv(1024)
    print("connection established:",data)
    sendingData(data)
    time.sleep(1)
    '''
    if you uncomment this code will not work
    stri=c_C.recv(1024)#can be used to receive data from TCP
    #print(stri.decode('utf-8'))
    if stri.decode('utf-8'):
        s_A1.send(bytes("request","utf-8"))
        '''
clt.close()
