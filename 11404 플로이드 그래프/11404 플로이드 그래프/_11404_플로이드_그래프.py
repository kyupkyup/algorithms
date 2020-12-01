N = int(input())
M = int(input())
result = [[0 for i in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if i!=j:
            result[i][j] = 10000000

for i in range(M):
    start, end, cost = map(int, input().split(" "))
    result[start-1][end-1] = min(result[start-1][end-1], cost)

def Floyd():
    global N, result
    for k in range(N):#경유노드
        for i in range(N):#출발노드
            for j in range(N):#도착노드
                result[i][j] = min(result[i][k] + result[k][j], result[i][j])

Floyd()
for i in range(N):
    for j in range(N):
        if(result[i][j] >= 10000000):
            result[i][j] = 0
        print(result[i][j], end=" ")
    print()   
