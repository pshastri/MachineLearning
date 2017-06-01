'''
Created on Jun 1, 2017

@author: pshastri
'''
'''
This code is to keep adding the test set to train set to make system more intelligent
'''

import numpy as np
import matplotlib.pyplot as mtp

def mindist(x,y):
    return np.sqrt(np.sum((x-y)**2))

X_trainset=np.array([[1,1],[4,4]])
Y_colorset=["red","green"]

mtp.figure()
mtp.scatter(X_trainset[:,0],X_trainset[:,1],s=100,c=Y_colorset[:])
mtp.show()

'''
Till here we have created one train set with 2 point. Now we will pass the test set
'''
X_testset=np.array([[1.1,3.3]])

'''
below calculate the minimum distance between the test point and train set point
'''
num1=len(X_trainset)
num2=len(X_testset)
for i in range(num2):
    mindist=np.zeros()