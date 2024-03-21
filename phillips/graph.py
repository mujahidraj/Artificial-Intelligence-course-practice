graph={
    0:[1,2,3],
    1:[5,6],
    2:[4],
    3:[4,2],
    4:[1],
    5:[],
    6:[4]
}

for i in graph:
    print(graph[i])
    for j in range(len(graph[i])):
        print(graph[i][j])