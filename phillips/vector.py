'''
To find the distance between the vectors
V1=⟨x1,y1,z1⟩ 
V2=⟨x2,y2,z2⟩
import math
d=math.sqrt((x1−x2)^2+(y1−y2)^2+(z1−z2)^2)
'''
import math
def distance(a,b):
    dis=0
    if len(a)==len(b):
        for i in range(len(a)):
            dis = dis+(a[i]-b[i])**2
    return math.sqrt(dis)
    

v1=[3,6,7]
v2=[8,9,2]
print(distance(v1,v2))