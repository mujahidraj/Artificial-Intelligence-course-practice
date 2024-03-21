def f(a=1,b=2):
    addition=a+b
    mult = a*b
    return addition,mult

result1, result2=f(100,200)
print(result1,result2)