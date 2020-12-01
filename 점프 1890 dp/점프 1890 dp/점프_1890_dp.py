
N = int(input())
route = [[map(int, input().split(" "))] for i in range(N)]

visitEnd = [False for in range(9223372036854775807)]

i=0
j=0
count=0
while 1:
    if(i + route[i][j] > N-1):
        continue
    elif(j + route[i][j]>N-1):
        continue
    else:
        i = i + route[i][j]
        j = j + route[i][j]
        if(route[i][j] == 0 and i==N-1 and j == N-1):
            visitedEnd[count] = True
            count += 1
        elif route[i][j] == 0:
            i = 0
            j = 0
        