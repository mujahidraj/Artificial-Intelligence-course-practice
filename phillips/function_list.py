def sumList(L):
    sum=0
    for i in range(len(L)):
        sum=sum+L[i]
    return sum

List=[10,20,30,40]
print(sumList(List))