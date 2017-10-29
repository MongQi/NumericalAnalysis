import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (pow(x,3)+4*pow(x,2)-10)
def func_zero(x1,y1,x2,y2):
    return(-(y1-x1*((y1-y2)/(x1-x2)))/((y1-y2)/(x1-x2)))
def func(x1,y1,x2,y2):
    k=(y1-y2)/(x1-x2)
    b=y1-x1*k
    sign = int((x2 - x1) / 0.01)
    dot1=np.arange(x1,x2,0.01)
    dot2=k*dot1+b
    return dot1,dot2
a=-1
b=2
x=np.arange(a,b,0.01)
sign=int((b-a)/0.01)
m=np.zeros((300))
plt.plot(x,f(x))
plt.plot(x,m)

for i in range(100):
    x_=func_zero(a,f(a),b,f(b))
    if((f(x_)*f(a))<0):
        b=x_
    else:
        a=x_
    if (np.abs(a-b)<0.01): break
    plt.pause(0.4)
    x_dot,y_dot=func(a,f(a),b,f(b))
    plt.plot(x_dot,y_dot)
    plt.pause(0.2)
    plt.scatter(x_,f(x_),c='r')
    m = np.arange(a, b, 0.01)
    print(x_,'  ',f(x_),'  ',a-b,'\n')



plt.show()
plt.close()
