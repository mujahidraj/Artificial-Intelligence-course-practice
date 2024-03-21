def linspace(lower,upper,n):
    L=[]
    h=(upper-lower)/n
    L.append(lower)
    for i in range(n-1):
        L.append(L[i]+h)
    L.append(upper)
    return L

print(linspace(0,1,5))