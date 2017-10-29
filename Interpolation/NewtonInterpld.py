# -*- coding:utf-8 -*-

import numpy as np

import matplotlib.pyplot as plt
import __future__
x=np.array([0.4,0.55,0.65,0.80,0.90,1.05])
y=np.array([0.41075,0.57815,0.69675,0.88811,1.02652,1.25382])

#牛顿插值

X=y
X=X.reshape([6,1])
for i in range (9):
    X=np.insert(X,1,values=np.zeros([6]),axis=1)

print (x,y)

for i in range(5):
    for j in range ((5-i)):
        X[j][i+1]=(X[j][i]-X[j+1][i])/(x[j]-x[j+i+1])

f_x=X[0][1:]
print (f_x)
def G(x,f_x,m,v):
    sum=0
    for i in range (4):
        s=1.0
        for j in range(i+1):
            s=s*(x-m[i])
        s=s*f_x[i]
        sum=sum+s
    sum=sum+v
    return sum

test_x=np.linspace(0.55,1.05,100,endpoint=True)
test_y=G(test_x,f_x,x,X[0][0])
plt.plot(test_x,test_y,lw=2)
print (G(1.05,f_x,x,X[0][0]))
plt.show()
