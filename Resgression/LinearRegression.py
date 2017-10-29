#-*- coding: utf-8 -*-
# #使用最小二乘法拟合一个直线
#实验数据
# xi | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
# yi |0.5|2.5| 2 | 4 |3.5| 6 |5.5|
# 首先我们会时候最小二乘法去拟合直线
# 然后使用 sklearn 中的 linearregression 模型去验证我们的结果
# 拟合结果会用 pyplot 库画图

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


def ls(x, y):
    # 线性回归 最小二乘拟合所需要计算的值
    # 设直线为Y=aX+b
    # | n   ∑Xi    |  | a |     |  ∑ Yi   |
    # |            |  |   |   = |         |
    # |∑Xi  ∑(Xi)² |  | b |     |  ∑Xi*Yi |
    n = x.shape[0]
    X_ = np.sum(x, axis=0)
    Y_ = np.sum(y, axis=0)
    X_Y = np.sum(x*y,axis=0)
    X_s = np.sum(np.square(x), axis=0)
    matrix_1=np.matrix([[n,     X_[0]],
                        [X_[0], X_s[0]]
                        ])
    matrix_2 = np.matrix([[Y_[0]],
                          [X_Y[0]]
                          ])
    a,b=matrix_1.I.dot(matrix_2)
    X_p = np.array([x[0], x[len(x) - 1]])
    Y_p = X_p * b + a
    plt.scatter(x, y,c='black')
    plt.plot(X_p, Y_p, 'r')
    plt.title(u"LeastSquares ( a = %f ) "% b)
    plt.show()
    plt.close()
    return b


def sk_ls(x,y):
    clf=LinearRegression()
    clf.fit(x,y)
    plt.scatter(x,y,c='blue')
    x_=[[0],x[0],x[6]]
    y_=clf.predict(x_)
    plt.plot(x_,y_,'green')
    plt.title(u"LinearRegression in sklearn( a = %f )"%clf.coef_)
    plt.show()
    plt.close()
    return clf.coef_


x=np.array([[1.],[2.],[3.],[4.],[5.],[6.],[7.]])
y=np.array([[0.5],[2.5],[2.],[4.],[3.5],[6.],[5.5]])
a1=ls(x,y)
a2=sk_ls(x,y)
if(a1-a2<0.001):print ('you are correct')









