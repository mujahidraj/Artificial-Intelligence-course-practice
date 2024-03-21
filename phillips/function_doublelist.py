def doubleList(L):
    L1=[]
    for i in range(len(L)):
        L1.append(L[i]*2)
    return L1

L=[10,20,30,40]
print(doubleList(L))