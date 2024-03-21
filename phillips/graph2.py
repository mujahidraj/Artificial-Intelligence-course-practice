def f(x):
    return x**2

def df(x):
    return 2*x

def linspace(lower,upper,n):
    L=[]
    h=(upper-lower)/n
    L.append(lower)
    for i in range(n-1):
        L.append(L[i]+h)
    L.append(upper)
    return L

Listx=linspace(-10,10,500)
Listy=[]
Listdf=[]
for i in range(len(Listx)):
    Listy.append(f(Listx[i]))
    Listdf.append(df(Listx[i]))
#print(Listx)
#print(Listy)
#print(Listdf)

import matplotlib.pyplot as plt
plt.plot(Listx,Listy)
plt.plot(Listx,Listdf)
plt.grid()
plt.show()