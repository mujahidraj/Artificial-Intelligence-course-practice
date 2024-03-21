import matplotlib.pyplot as plt
import math


def f(x):
    return 1/(1+math.exp(-x))

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
for i in range(len(Listx)):
    Listy.append(f(Listx[i]))
#print(Listx)
#print(Listy)
#print(Listdf)

import matplotlib.pyplot as plt
plt.plot(Listx,Listy)
plt.grid()
plt.show()