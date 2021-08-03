import socket
import random
import time
import pickle


host=socket.gethostbyname(socket.gethostname())#to know the host name
port=5325
s_A=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#to create socket
s_A.bind((host,port))#assign ip address and port number to socket
s_A.listen(5)#listen to incoming connections
c_B, adr=s_A.accept()#




#for sending random data from slave to master
def sendingData():
    n = random.randint(0,100)  #for generating random data in range 0 to 100
    print(n)
    st=pickle.dumps(n)#st=str(st)for serializing data
    c_B.send(st)#clt.send(bytes(st,'utf-8'))for sending data

while True:
    #clt, adr =s.accept()#accepts an incoming connection request from a TCP client
    print("connection established:",adr)
    sendingData()
    time.sleep(1)
    '''
    if u uncomment this code it wont work
    stri=c_B.recv(1024)#can be used to receive data from TCP
        #print(stri.decode('utf-8'))
    if stri.decode('utf-8'):
        for i in range(20):
            sendingData()
            time.sleep(0.5)'''
clt.close()



