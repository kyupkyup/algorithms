
N, S, M = map(int, input().split(" "))
volumeList = map(int, input().split(" "))
MAX = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    for j in range(i+1):
        if j==0 :
            MAX[i][j] = MAX[i-1][j] + arr[i][j]
        elif j==i:
            MAX[i][j] = MAX[i-1][j-1] + arr[i][j]
        else:
            MAX[i][j] = max(MAX[i-1][j-1] + arr[i][j], MAX[i-1][j] + arr[i][j])