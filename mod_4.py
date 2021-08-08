import socket
import pickle
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import logging
import numpy as np
from logging.handlers import RotatingFileHandler

host = socket.gethostbyname(socket.gethostname())  # "192.168.43.200" # client ip "192.168.43.128
port = 5555
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
x, y = [], []
Ti = []
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)
# add a rotating handler
handler = RotatingFileHandler("data.txt", maxBytes=2000, backupCount=1)
logger.addHandler(handler)


def animate(i, x, y, logger):
    msg = client.recv(1024)
    p = pickle.loads(msg)
    x.append(p)
    # y.append(p[1])
    Tim = dt.datetime.now().strftime('%H:%M:%S')
    Ti.append(Tim)
    ax.clear()
    ax.plot(Ti, x)
    # ax.plot(Ti,y)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Temperature over Time')
    plt.xlabel('time')
    logger.info(f"time and date={Tim},temparature={p}")


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(x, y, logger), interval=1000)
plt.show()
