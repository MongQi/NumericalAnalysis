import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random_integers

def f(x):
    return (pow(x,3)+4*pow(x,2)-10)

def error_rate(x_old,x_new):
    return (np.abs((x_new-x_old)))

def function0(x):
    return np.min(np.abs(x))

a=-1
b=2
x=np.arange(a,b,0.01)
sign=int((a-b)/0.01)
m=np.zeros((300))
plt.plot(x,f(x))
plt.plot(x,m)
print (f(1))
a=-1
b=2
x_=0

plt.ion()
for i in range(100):
    x_=(a+b)/2
    if((f(x_)*f(a))<0):
        b=x_
    else:
        a=x_
    if(error_rate(a,b)<pow(10,-15)):break
    plt.pause(0.5)
    plt.scatter(x_,f(x_),c='r')
    m = np.arange(a, b, 0.01)
    print(x_,'  ',f(x_),'\n')

plt.show()
plt.close()

