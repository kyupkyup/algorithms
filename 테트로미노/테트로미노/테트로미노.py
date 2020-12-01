N, M = map(int, input().split(" "))

board = [list(map(int, input().split(" "))) for _ in range(N)]

def solution():
    answer = []
    for i in range(N):
        for j in range(M):
            answer.append(tetromino(i, j))
    return max(answer)

def tetromino(y, x):
    result = []
    if x+1 < M and x+2 < M and x+3 < M: # 가로 네 줄 
        result.append(board[y][x]+board[y][x+1]+ board[y][x+2]+ board[y][x+3])
    if y+1 < N and y+2 < N and y+3 < N: # 세로y 네 줄
        result.append(board[y][x]+board[y+1][x]+ board[y+2][x]+ board[y+3][x])
    if x+1 < M and y+1 < N: # 네모난 모양
        result.append(board[y][x]+board[y][x+1]+ board[y+1][x]+ board[y+1][x+1])
    if y+1 < N and y+2 <N and x+1 <M: # 세번째 노대칭
        result.append(board[y][x]+board[y+1][x]+ board[y+2][x]+ board[y+2][x+1])
    if x+1 < M and x+2 <M and y -1 >= 0: 
        result.append(board[y][x]+board[y][x+1]+ board[y][x+2]+ board[y-1][x])    
    if y-1 >=0 and y-2 >=0 and x-1>=0:
        result.append(board[y][x]+board[y-1][x]+ board[y-2][x]+ board[y-2][x-1])    
    if x-1 >=0 and x-2>=0 and y+1 < N:
        result.append(board[y][x]+board[y][x-1]+ board[y][x-2]+ board[y+1][x-2])        
    if y+1 < N and y+2 < N and x-1>=0: #대칭 부
        result.append(board[y][x]+board[y+1][x]+ board[y+2][x]+ board[y+2][x-1])
    if x-1 >= 0 and x-2 >=0 and y-1 >=0:
        result.append(board[y][x]+board[y][x-1]+ board[y][x-2]+ board[y-1][x-2])
    if y-1 >=0 and y-2 >=0 and x+1 < M:
        result.append(board[y][x]+board[y-1][x]+ board[y-2][x]+ board[y-2][x+1])
    if x+1 < M and x+2 <M and y+1 < N:
        result.append(board[y][x]+board[y][x+1]+ board[y][x+2]+ board[y+1][x+2])
    if x+1 <M  and y + 2 < N: # 네번쨰 꺼 노대칭
        result.append(board[y][x]+board[y+1][x]+ board[y+1][x+1]+ board[y+2][x+1])    
    if x-2>=0 and y+1 < N:
        result.append(board[y][x]+board[y][x-1]+ board[y+1][x-1]+ board[y+1][x-2])    

    if x-1 >=0 and y-2 >=0:
        result.append(board[y][x]+board[y-1][x]+ board[y-1][x-1]+ board[y-2][x-1])
    if x+2< M and y-1 >=0:
        result.append(board[y][x]+board[y][x+1]+ board[y-1][x+1]+ board[y-1][x+2])    
    if x-1 >=0 and y+2 <N:   #네번째 꺼 대칭
        result.append(board[y][x]+board[y+1][x]+ board[y+1][x-1]+ board[y+2][x-1])    

    if x-2>=0 and y-1 >=0:
        result.append(board[y][x]+board[y][x-1]+ board[y-1][x-1]+ board[y-1][x-2])
    if x+1 < M and y-2>=0:
        result.append(board[y][x]+board[y-1][x]+ board[y-1][x+1]+ board[y-2][x+1])
    if x+2<M and y-1 >=0:
        result.append(board[y][x]+board[y][x+1]+ board[y-1][x+1]+ board[y-1][x+2])
    if x+2<M and y+1 <N: # 다섯번쨰 노대칭
        result.append(board[y][x]+board[y][x+1]+ board[y+1][x+1]+ board[y][x+2])
    if x-1>=0 and y+2 <N:
        result.append(board[y][x]+board[y+1][x]+ board[y+1][x-1]+ board[y+2][x-1])
    if x-2 >=0 and y-1 >=0:
        result.append(board[y][x]+board[y][x-1]+ board[y][x-2]+ board[y-1][x-1])
    if y-2 >=0 and x+1 <M:
        result.append(board[y][x]+board[y-1][x]+ board[y-1][x+1]+ board[y-2][x+1])
    if x+2 <M and y-1 >=0: # 다섯번쨰 데칭
        result.append(board[y][x]+board[y][x+1]+ board[y-1][x+1]+ board[y][x+2])        
    if y+2 < N and x+1 <M:
        result.append(board[y][x]+board[y+1][x]+ board[y+1][x+1]+ board[y+2][x+1])
    if x-2 >=0 and y + 1< N:
        result.append(board[y][x]+board[y][x-1]+ board[y+1][x-1]+ board[y][x-2])
    if y-2 >=0 and x-1 >=0:
        result.append(board[y][x]+board[y-1][x]+ board[y-1][x-1]+ board[y-2][x-1])
    return max(result)
print(solution())