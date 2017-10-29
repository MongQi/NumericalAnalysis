import numpy as np
import matplotlib.pyplot as plt

class Interpolation_Lagrange:
    def __init__(self):
        self.coef=None
        x_set=None
        y_set=None
    def Fit(self,x, y):
        """
        Inputs:
        - X  :  A list or a ndarray of shape (N,)
        - Y  :  A list or a ndarray of shape (N,)
        """
        self.x_set=np.array(x)
        self.y_set=np.array(y)
        if self.coef is None:
            self.coef = np.array([])
        num = len(self.x_set)
        for i in range(num):
            self.coef = np.append(self.coef, self.y_set[i])
            for j in range(num):
                if (i != j): self.coef[i] = self.coef[i] /(self.x_set[i] - self.x_set[j])
        print ('all work have finished')
    def f_(self,x):
        result=0
        length=len(self.x_set)
        for i in range(length):
            sum=1
            for j in range(length):
                if (i!=j):
                    sum= sum*(x - self.x_set[j])
            result=result+self.coef[i]*sum
        return result
    def predict(self,x_in):
        """
        Inputs:
        - X_in  :  A list or a ndarray of shape (N,)

        Returns:
        - y_pred:  Predicted y for the data in X,
        """
        length=len(x_in)
        result=np.zeros(length)
        for m in range(length):
            result[m]=self.f_(x_in[m])
        return result
    def show(self):
        #show result that you have fit as a picture in pyplot
        plt.scatter(self.x_set,self.y_set,c='b')
        x_p=np.arange(np.min(self.x_set),np.max(self.x_set),0.001)
        y_p=self.predict(x_p)
        plt.plot(x_p,y_p,c='y')

        plt.show()
        plt.close()


"""
x=[1,3,2]
y=[1,2,-1]
pred_x=[1.5]
"""

x=[0.4,0.55,0.65,0.80,0.90,1.05]
y=[0.41075,0.57815,0.69675,0.88811,1.02652,1.25382]
pred_x=[0.596]

"""
x=[1,4,6]
y=[0,1.3863,1.7918]
pred_x=[2.0]
"""
model=Interpolation_Lagrange()
model.Fit(x,y)
pred=model.predict(pred_x)
plt.scatter(pred_x,pred,c='r')
model.show()
