from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

#使用最小二乘法拟合一个 曲线
#实验数据
# xi |  0  |  1  |  2  |  3  |  4  |  5  |
# yi | 2.1 | 7.7 |13.6 |27.2 |40.9 |61.1 |
#在函数中会使用sklearn中的多项式回归进行验证

def pr(x,y):
# 线性回归 最小二乘拟合所需要计算的值
# 设直线为Y=A2*X²+A1*X+A3
# |  n       ∑Xi   ∑(Xi)² |  | A0 |     |  ∑ Yi   |
# | ∑Xi    ∑(Xi)²  ∑(Xi)³ |  | A1 |   = | ∑Xi*Yi  |
# |∑(Xi)²  ∑(Xi)³  ∑(Xi)^4|  | A2 |     | ∑Xi²*Yi |
    N=x.shape[0]
    X_  = np.sum(x,axis=0)
    Y_  = np.sum(y,axis=0)
    X_2 = np.sum(np.square(x),axis=0)
    X_3 = np.sum(np.power(x,3),axis=0)
    X_4 = np.sum(np.power(x,4),axis=0)
    X_Y = np.sum(x*y,axis=0)
    X2_Y= np.sum(np.square(x)*y,axis=0)
    matrix_1=np.matrix([[N,     X_[0],  X_2[0]],
                        [X_[0], X_2[0], X_3[0]],
                        [X_2[0],X_3[0], X_4[0]]
                        ])
    matrix_2=np.matrix([[Y_[0]],
                        [X_Y[0]],
                        [X2_Y[0]]
                        ])
    a0,a1,a2=matrix_1.I.dot(matrix_2)
    X_p=np.arange(np.min(x),np.max(x),0.01)
    X_p=X_p.reshape(np.shape(X_p)[0],1)
    Y_p=np.square(X_p)*a2+X_p*a1+a0
    plt.plot(X_p,Y_p,c='black')
    #plt.plot(X_p,Y_p-1,c='black')
    #可使用对比两条线的形状，二者重合不易观察
    plt.scatter(x,y,c='blue')
    #下面以sklearn中的多项式回归进行验证，画以红线
    poly_reg= PolynomialFeatures(degree=2)
    X_p = np.arange(np.min(x), np.max(x), 0.01)
    X_p = X_p.reshape(np.shape(X_p)[0], 1)
    X_poly=poly_reg.fit_transform(x)
    clf=LinearRegression()
    clf.fit(X_poly,y)
    Y_p=clf.predict(poly_reg.fit_transform(X_p))
    plt.plot(X_p, Y_p, c='r')
    plt.scatter(x, y, c='blue')
    plt.show()
    plt.close()

x = np.array([[0.], [1.], [2.],  [3.],  [4.],  [5.]  ])
y = np.array([[2.1],[7.7],[13.6],[27.2],[40.9],[61.1]])
pr(x,y)