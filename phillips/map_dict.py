# Map --- dict
student={100:"Richard",200:"Jonathan",300:"Mr p."}

for i in student.keys():
    print(i, student[i])

student[400]="Florence" # add element in map or dict

for i in student.values():
    print(i)

for i in student:
    print(i, student[i])