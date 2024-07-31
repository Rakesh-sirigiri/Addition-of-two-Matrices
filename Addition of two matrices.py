X = [[1,2,3],
     [4,5,6],
     [6,7,8]]
Y = [[3,4,5],
     [4,5,7],
     [2,3,7]]
result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]

for r in result:
    print(r)
