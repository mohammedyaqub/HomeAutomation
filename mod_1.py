import threading
import socket
import time
import pickle
import random

def send_data(so,i):
    data=random.randint(0,40)
    print(data)
    so.send(pickle.dumps(data))
    time.sleep(i)

def rec(so,s,flag):
    while True:
        print("1")
        data=so.recv(1024)
        print(data)
        if data:
            flag=1




host=socket.gethostbyname(socket.gethostname())
port=9999
port2=1222
flag=0
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(4)
print("connected")
ctl,addr=s.accept()
print("accept")
t=threading.Thread(target=rec,args=(ctl,s,flag))
t.start()
while True:
    send_data(ctl,2)
    print("data sent")
    '''ctl.send(bytes("hello","utf-8"))
    time.sleep(1)'''
    if flag==1:
        for i in range(30):
            send_data(ctl,1)
        flag=0
    #t.start()
    time.sleep(2)
s.close()







