import socket
import threading
import time

def rec(so,s):
    while True:
        data=so.recv(1024)
        if data:
            s.send(data)

host = socket.gethostbyname(socket.gethostname())
port = 9999
port2 = 1222
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect((host, port))
s2=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind((host,port2))
s2.listen(4)
c2,ad2=s2.accept()
print(c2,ad2)
t = threading.Thread(target=rec, args=(c2,s))

try:
    s.connect((host, port))
    t.start()
    #s.send(bytes("hello", "utf-8"))
    while True:
        msg=s.recv(1024)
        c2.send(msg)
        print(msg)
        time.sleep(2)
finally:
    s.close()
    t.join()
