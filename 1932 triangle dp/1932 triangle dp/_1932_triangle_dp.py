
N = int(input())
arr = [list(map(int, input().split(" "))) for i in range(N)]
result= arr[0][0]
MAX = [[0 for i in range(500)] for i in range(500)] 

i = 0
for i in range(1, N):
    for j in range(i+1):
        if j==0 :
            MAX[i][j] = MAX[i-1][j] + arr[i][j]
        elif j==i:
            MAX[i][j] = MAX[i-1][j-1] + arr[i][j]
        else:
            MAX[i][j] = max(MAX[i-1][j-1] + arr[i][j], MAX[i-1][j] + arr[i][j])
print(MAX)
#sum = -1000
#for i in range(N):
#    if(MAX[i][i] > sum ):
#        sum = MAX[i][j]


