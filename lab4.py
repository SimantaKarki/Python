# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0,9.0)

#preprocessing 
data = pd.read_csv('data.csv')
X = data.iloc[:,0]
Y = data.iloc[:,1]
plt.scatter(X,Y)
plt.show()

#building model
m = 0;
c = 0;
L = 0.0001 #learning rate
epochs = 1000 #no fo iterations to perform gradinet descent
n = float(len(X))

#performing gradient descent
for i in range(epochs):
    Y_predict  = m*X + c # the current predicted value of Y
    D_m =(-2/n)*sum(X*(Y-Y_predict)) #derivative wrt m
    D_c = (-2/n)*sum(Y-Y_predict) #derivative wrt c
    m = m-L*D_m #update m
    c = c-L*D_c #update c
    print(m,c)
    
#making predictions
Y_pred = m*X +c
plt.scatter(X, Y)
plt.plot([min(X),max(X)],[min(Y_predict),max(Y_predict)])
plt.show()
