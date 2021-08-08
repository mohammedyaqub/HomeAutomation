import socket
import pickle

host = socket.gethostbyname(socket.gethostname())  # to know the host name
port = 1222
port1 = 5555
s_B = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to create socket
s_B.connect((host, port))
print("connted")
s_f=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_f.bind((host,port1))
s_f.listen(3)
clt,addr=s_f.accept()
print("ok")
#s_B.connect((host, port))
while True:
    st = s_B.recv(1024) # can be used to receive data from TCP
    clt.send(st)
    print(pickle.loads(st))
    if pickle.loads(st)<=10:
        s_B.send(bytes("request","utf-8"))
    elif pickle.loads(st)>=30:
        s_B.send(bytes("request","utf-8"))

