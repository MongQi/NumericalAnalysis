import numpy as np
import matplotlib.pyplot as plt

def f_(x):
    return (3*np.exp(x)-np.cos(x)*4)
def d_fx(x):#对f（x）进行求导操作
    return (3*np.exp(x)+4*np.sin(x))
def x_line(x,y,k):#求直线与X轴的交点
    return x-y/k
x=np.arange(0,1.3,0.01)
y=f_(x)
plt.plot(x,y,'pink')
plt.xlim(0,1.3)
X=np.arange(0,1.3,0.01)
Y=np.zeros(X.size)
plt.plot(X,Y,"black")
x_start=1
plt.ion()
for i in range(30):
    plt.scatter(x_start,0,c='r')
    y_start=f_(x_start)
    yp=np.arange(0,y_start,0.01)
    xp=np.ones(yp.size)*x_start
    plt.plot(xp,yp,'blue')
    plt.pause(0.3)
    k=d_fx(x_start)
    x_next=x_line(x_start,y_start,d_fx(x_start))
    y_next=0
    xp=np.arange(x_next,x_start,0.01)
    yp=d_fx(x_start)*xp+y_start-d_fx(x_start)*x_start
    plt.plot(xp,yp,'r')
    #if((x_start-x_next)<0.001):break
    x_start=x_next
    y_start=y_next
    plt.pause(0.8)


plt.show()
plt.close()
