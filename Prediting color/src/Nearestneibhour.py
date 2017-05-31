'''
Created on May 29, 2017
 
@author: pshastri
'''
import numpy as np 
import matplotlib.pyplot as plt 

def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))


X_train=np.array([[1,1],[2,2],[3,3],[4,4]])
Y_train=["red","red","yellow","yellow"]

X_test=np.array([[1,2],[2.1,3]])
Y_test=[]
plt.figure()
plt.scatter(X_train[:,0], X_train[:,1], s=170, color=Y_train[:])

num=len(X_train)
num1=len(X_test)
# leastdist=np.zeros(num)
# print leastdist
for j in range(num1):
    leastdist=np.zeros(num)
    print j
    for i in range (num):
        leastdist[i]=dist(X_train[i],X_test[j])
    print leastdist
    min_index=np.argmin(leastdist)
    Y_test.append(Y_train[min_index])

plt.scatter(X_test[:,0], X_test[:,1], s=170, color=Y_test[:])
plt.show()
# print (Y_train[min_index])