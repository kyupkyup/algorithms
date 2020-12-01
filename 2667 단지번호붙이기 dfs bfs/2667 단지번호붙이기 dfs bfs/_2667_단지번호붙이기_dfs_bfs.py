
N = int(input())

matrix = [list(map(int, input())) for _ in range(N)]
visit = [[0] * (N) for _ in range(N)]

count = 0

def dfs(startX, startY):
    global matrix, visit, count


    if startX < 0 or startX >= N or startY < 0 or startY >= N:
        return 

    if visit[startY][startX] == 1:
        return 
    else:
        visit[startY][startX] = 1

    if matrix[startY][startX] == 0:
        return 

    
    count += 1 
    dfs(startX+1, startY)
    dfs(startX-1, startY)
    dfs(startX, startY+1)
    dfs(startX, startY-1)
    return count

countList = []
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1 and visit[i][j] == 0:
            count = 0
            countList.append(dfs(j, i))
            
print(len(countList))
countList.sort()
for i in range(len(countList)):
    print(countList[i])
