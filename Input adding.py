# Defined array
array = [10, 20, 30, 40, 50]

output = [array[0]]

for i in range(1, len(array)):
    output.append(array[i] + output[i - 1])

print(output)
