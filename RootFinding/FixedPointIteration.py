import numpy as np
import matplotlib.pyplot as plt

def f_(x):
    return x
def F_(x):
    return x
def g_(x):
    return np.sqrt(2)*np.sqrt(x)
x=np.arange(0,4,0.01)
Z=x*0
plt.plot(x,f_(x),c='g')
plt.plot(x,g_(x),c='blue')
plt.xlim(0,4)
plt.ylim(0,4)
plt.ion()
x_start=0.1
plt.scatter(x_start,0,c='r')
for i in range(30):
    y_start=f_(x_start)
    x_next=x_start
    y_next=g_(x_next)
    plt.scatter(x_start,y_start,c='r')
    plt.scatter(x_next,y_next,c='r')
    yp = np.arange(y_start,y_next,0.01)
    xp = np.ones(yp.size)*x_start
    plt.plot(xp, yp, c="r")
    x_start = x_next
    y_start = y_next
    plt.pause(0.2)
    #前半段
    x_next=F_(y_start)
    plt.scatter(x_start,y_next,c="r")
    plt.scatter(x_next, y_next, c='r')
    xp=np.arange(x_start,x_next,0.01)
    yp=np.ones(xp.size)*y_start
    plt.plot(xp,yp,c="r")
    x_start = x_next
    y_start = y_next
    plt.pause(0.4)
    plt.scatter(x_start, 0, color='r')
plt.show()
plt.close()
