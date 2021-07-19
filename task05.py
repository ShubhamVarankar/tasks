import numpy as np

def getA(X, B, C):
    BC = np.dot(B,C)
    A0 = (X-BC[1][0])/(BC[0][0]-BC[1][0])
    print (round(A0,2),end=" ")
    print (round(1-A0,2))
    return

testcases = int(input())
for i in range(testcases):
    X = float(input())
    B = np.reshape(np.array(input().split(), dtype='float'),(2,2))
    C = np.reshape(np.array(input().split(), dtype='float'),(2,1))
    getA(X, B, C)