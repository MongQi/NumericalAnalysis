import numpy as np
import matplotlib.pyplot as plt
import pylab
pylab.mpl.rcParams['font.sans-serif'] = ['SimHei']
pylab.mpl.rcParams['axes.unicode_minus'] = False

class SplineInterpolation:
    def __init__(self,X=None,y=None):
        self.X=np.array(X)
        self.y=np.array(y)
        self.CubicAns=None
        self.QuadraticAns=None

    def QuadraticSI(self):
        X=self.X
        y=self.y
        matrix_l=np.zeros([3*(len(X)-1)-1,3*(len(X)-1)-1])
        matrix_r=np.zeros([3*(len(X)-1)-1,1])
        for i in range(len(X)-1):
            if(i==0):
                matrix_l[i][0]=X[i+1]
                matrix_l[i][1]=1
                matrix_r[i]=y[i+1]
            if(i!=0 and i!=len(X)-2):
                matrix_l[2*i-1][3 * i -1] = X[i] * X[i]
                matrix_l[2*i-1][3 * i +0] = X[i]
                matrix_l[2*i-1][3 * i +1] = 1
                matrix_r[2*i-1] = y[i]
                matrix_l[2*i][3 * i -1] = X[i+1] * X[i+1]
                matrix_l[2*i][3 * i +0] = X[i+1]
                matrix_l[2*i][3 * i +1] = 1
                matrix_r[2*i] = y[i+1]
            if(i==(len(X)-2)):
                matrix_l[2 * i - 1][3*(len(X)-1)-4] = X[i] * X[i]
                matrix_l[2 * i - 1][3*(len(X)-1)-3] = X[i]
                matrix_l[2 * i - 1][3*(len(X)-1)-2] = 1
                matrix_r[2 * i - 1] = y[i]

        start = 2 * (len(X) - 2)
        matrix_l[start][0]=X[0]
        matrix_l[start][1]=1
        matrix_r[start]=y[0]
        start=start+1
        matrix_l[start][3*(len(X)-1)-1-3]=X[len(X)-1]*X[len(X)-1]
        matrix_l[start][3*(len(X)-1)-3]=X[len(X)-1]
        matrix_l[start][3 * (len(X) - 1) - 2]=1
        matrix_r[start]=y[len(X)-1]
        start=start+1
        for i in range(len(X)-1):
            if (i!=0 and i==1):
                matrix_l[start][0]=1
                matrix_l[start][3*i-1]=-2*X[i]
                matrix_l[start][3*i]=-1
                start=start+1
            if (i!=0 and i!=1):
                matrix_l[start][3*(i-1)-1]=2*X[i]
                matrix_l[start][3* (i - 1)] = 1
                matrix_l[start][3 * i - 1] = -2 * X[i]
                matrix_l[start][3 * i] = -1
                start = start + 1
        ans=np.dot(np.linalg.inv(matrix_l),matrix_r)
        ans=np.insert(ans,0,[0],axis=0)
        self.QuadraticAns=ans

    def CubicSI(self):
        X = self.X
        y = self.y
        matrix_l=np.zeros([4*(len(X)-1),4*(len(X)-1)])
        matrix_r=np.zeros([4*(len(X)-1),1])
        for i in range(len(X)-1):
            if(i==0):
                matrix_l[i][i*i+0]=X[1]**3
                matrix_l[i][i*i+1]=X[1]**2
                matrix_l[i][i*i+2]=X[1]
                matrix_l[i][i*i+3]=1
                matrix_r[0]=y[1]

            if(i!=0 and i!=len(X)-2):
                matrix_l[2*i-1][4 * i +0]=X[i]**3
                matrix_l[2*i-1][4 * i +1] = X[i] **2
                matrix_l[2*i-1][4 * i +2] = X[i]
                matrix_l[2*i-1][4 * i +3] = 1
                matrix_r[2*i-1] = y[i]
                matrix_l[2*i][4 * i +0] = X[i+1] ** 3
                matrix_l[2*i][4 * i +1] = X[i+1] * X[i+1]
                matrix_l[2*i][4 * i +2] = X[i+1]
                matrix_l[2*i][4 * i +3] = 1
                matrix_r[2*i] = y[i+1]
            if(i==(len(X)-2)):
                matrix_l[2 * i - 1][-4] = X[i] ** 3
                matrix_l[2 * i - 1][-3] = X[i] * X[i]
                matrix_l[2 * i - 1][-2] = X[i]
                matrix_l[2 * i - 1][-1] = 1
                matrix_r[2 * i - 1] = y[-2]


        start = 2 * (len(X) - 2)
        matrix_l[start][0] = X[0]**3
        matrix_l[start][1] = X[0]**2
        matrix_l[start][2] = X[0]**1
        matrix_l[start][3] = 1
        matrix_r[start] = y[0]
        start = start + 1

        matrix_l[start][-4] = X[-1] ** 3
        matrix_l[start][-3] = X[-1] **2
        matrix_l[start][-2] = X[-1]**1
        matrix_l[start][-1] = 1
        matrix_r[start] = y[-1]
        start = start + 1

        for i in range(len(X)-1):
            if(i!=1):
                matrix_l[start][4*(i-1)]=6*X[i]
                matrix_l[start][4*(i-1)+1] = 2
                matrix_l[start][4*(i)]= -6 * X[i]
                matrix_l[start][4*(i)+1]= -2
                start = start + 1

        for i in range(len(X)-1):
            if(i!=0):
                matrix_l[start][4 * (i-1)] = 3 *(X[i]**2)
                matrix_l[start][4 * (i-1) + 1] = 2 *X[i]
                matrix_l[start][4 * (i-1) + 2] = 1
                matrix_l[start][4 * i] = -3 *(X[i]**2)
                matrix_l[start][4 * i+1] = -2 *X[i]
                matrix_l[start][4 * i+2] = -1
                start = start + 1
        matrix_l[start][0] = 6 * X[0]
        matrix_l[start][1] = 2
        start = start + 1
        matrix_l[start][-1] = 6 * X[-1]
        matrix_l[start][-2] = 2
        ans = np.dot(np.linalg.inv(matrix_l), matrix_r)
        self.CubicAns=ans

    def show(self):
        if(self.QuadraticAns is None and self.CubicAns is not None):
            X = self.X
            y = self.y
            ans = self.CubicAns
            for i in range(len(X) - 1):
                x_pl = np.arange(X[i], X[i + 1], 0.01)
                y_pl = ans[4 * i + 0][0] * (x_pl ** 3) + \
                       ans[4 * i + 1][0] * (x_pl ** 2) + \
                       ans[4 * i + 2][0] * x_pl + \
                       ans[4 * i + 3][0]
                plt.plot(x_pl, y_pl)
            plt.scatter(X, y, c='r')
            plt.title(u"三次样条插值")
            plt.show()
            plt.close()
        elif (self.QuadraticAns is not None and self.CubicAns is  None):
            X = self.X
            y = self.y
            ans = self.QuadraticAns
            for i in range(len(X) - 1):
                x_pl = np.arange(X[i], X[i + 1], 0.01)
                y_pl = ans[3 * i + 0][0] * np.square(x_pl) + ans[3 * i + 1] * (x_pl) + ans[3 * i + 2]
                plt.plot(x_pl, y_pl)
            plt.scatter(X, y, c='r')
            plt.title(u"二次样条插值")
            plt.show()
            plt.close()
        elif(self.QuadraticAns is not None and self.CubicAns is not None):
            fig=plt.figure()
            ax=fig.add_subplot(2,1,1)
            X=self.X
            y=self.y
            ans=self.QuadraticAns
            for i in range(len(X)-1):
                x_pl=np.arange(X[i],X[i+1],0.01)
                y_pl=ans[3*i+0][0]*np.square(x_pl)+ans[3*i+1]*(x_pl)+ans[3*i+2]
                ax.plot(x_pl,y_pl)
            ax.scatter(X,y,c='r')
            ax.text(6.5,1,u"二次样条插值")
            ax=fig.add_subplot(2,1,2)
            ans=self.CubicAns
            for i in range(len(X) - 1):
                x_pl = np.arange(X[i], X[i + 1], 0.01)
                y_pl = ans[4 * i + 0][0] * (x_pl**3) + \
                       ans[4 * i + 1][0] * (x_pl**2) + \
                       ans[4 * i + 2][0]*x_pl+\
                       ans[4 * i + 3][0]
                ax.plot(x_pl, y_pl)
            ax.scatter(X, y, c='r')
            ax.text(6.5,1,u"三次样条插值")
            plt.show()



X=[3,4.5,7,9,11]
y=[2.5,1,2.5,0.5,25]
clf=SplineInterpolation(X,y)
#clf.QuadraticSI()
clf.CubicSI()
clf.show()
