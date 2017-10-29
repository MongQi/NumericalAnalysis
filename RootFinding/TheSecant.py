import numpy as np
import matplotlib.pyplot as plt


def f_(x):
    return (3*np.exp(x)-np.cos(x)*4)

x=np.arange(0,1.3,0.01)
y=f_(x)
plt.plot(x,y,'pink')
plt.xlim(0,1.3)
X=np.arange(0,1.3,0.01)
Y=np.zeros(X.size)
plt.plot(X,Y,"black")
x_start_1=1
x_start_2=0.9
for i in range(30):
    y_start_1=f_(x_start_1)
    y_start_2=f_(x_start_2)
    plt.scatter(x_start_1,y_start_1,c='b')
    plt.scatter(x_start_2,y_start_2,c='b')
    plt.pause(0.2)
    k_lin=(y_start_1-y_start_2)/(x_start_1-x_start_2)#割线斜率
    b_lin=y_start_1-x_start_1*k_lin
    x_lin=x_start_1-(y_start_1/k_lin)#割线与x轴的交点
    xp=np.arange(x_lin,x_start_1,0.01)
    yp=k_lin*xp+b_lin
    plt.plot(xp,yp,c='r')
    x_start_1=x_start_2
    y_start_1=y_start_2
    x_start_2=x_lin
    y_start_2=f_(x_start_2)
    plt.pause(0.2)









plt.show()
plt.close()