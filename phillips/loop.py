# range(5) -----> i=0, i<5 , i+=1
# range(2,5) ----> i =2, i<5, i+=1
# range(2,5,1) ---> i=2,i<5, i+=1
# range(2,5,2) ---> i=2,i<5, i+=2

for i in range(5):
    print(i,end=" ")
    
print()

for i in range(2,5):
    print(i,end=" ")

print()

for i in range(2,10,2):
    print(i,end=" ")