
import pickle, time
import socket

host = socket.gethostbyname(socket.gethostname())  # to know the host name
port = 1124
port1 = 5555
s_C=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_C.bind((host,port1))
s_C.listen(3)#listen to incoming connections
c_D, adr=s_C.accept()#
s_B = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # to create socket
s_B.connect((host, port))
print("connected")




# to request data from slave
def requestData():
    s_B.send(bytes("requested", 'utf-8'))  # used to send data from one socket to another socket.
    #st = s_B.recv(1124)  # can be used to receive data from TCP
    #data = pickle.loads(st)  # to serialize data
    #return data


def main():
    # for i in range(20):
    #c_D, adr = s_C.accept()
    #print(adr,c_D)
    while True:
        st = s_B.recv(1124)  # can be used to receive data from TCP
        print(st)
        c_D.send(st)
        #c_D, adr = s_C.accept()
        #print(adr,c_D)
        data = pickle.loads(st)
        if data is not None:
            if data <= 10:
                print("switch on the heater", data)
                requestData()
            elif data >= 40:
                print("switch on the cooler", data)
                requestData()
            else:
                print("there is no harm,stable condition", data)



if __name__ == '__main__':
    main()
