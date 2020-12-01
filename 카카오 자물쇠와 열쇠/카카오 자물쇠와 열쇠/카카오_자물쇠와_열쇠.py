
import copy
# 7.4%

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
count = -1

def solution(key, lock):
    # 90도 회전, 270도 회전 상하좌우 이동 
    # 배열 밖으로 나가는 부분을 어떻게 처리할지?
    temp = len(key)
    new_key_arr = [[0 for i in range(temp*3)] for i in range(temp*3)]
    answer = False
    for i in range(temp*3):
        for j in range(temp*3):
            if (i >= temp and i < temp*2) and (j>=temp and j<temp*2):
                new_key_arr[j][i] = key[j-temp][i-temp]

    
    answer = bfs(new_key_arr, lock, temp)
    return answer
    # key 2중 for 문 돌려서 모든 값의 가로 값 더하기 만약 오버되면 

def bfs(key, lock, temp):
    global count
    # KEY와 LOCK이 맞는지 확인. 
    if count >= 4 * temp ** 4:
        return False

    temp_lock = copy.deepcopy(lock)
    for i in range(temp):
        for j in range(temp):
            if lock[j][i] == 0 and key[j+temp][i+temp] == 1:
                temp_lock[j][i] = 1
    cnt = 0
    for i in range(temp):
        if 0 in temp_lock[i]:
            cnt +=1
    if cnt == 0:
        return True

    else:
        count += 1
    # 안맞으면 회전 BFS 2개,  이동 BFS 4개  만들어줌
        count = bfs(move(key,1, temp), lock, temp)
        count = bfs(move(key,2, temp), lock, temp)
        count = bfs(move(key,3, temp), lock , temp)
        count = bfs(move(key,4, temp), lock, temp)
        count = bfs(_90rotate(key), lock, temp)
        count = bfs(_270rotate(key), lock, temp)

        
        return count

def move(key, value, temp):

    # 1 오른쪽 , 2 왼쪽 3 위 4 아래
    if value == 1:
        for i in range(temp, temp*2):
            for j in range(temp, temp*2):
                if key[j][i] == 1:
                    key[j][i] = 0
                    key[j][i+1] = 1 
    elif value == 2:
        for i in range(temp, temp*2):
            for j in range(temp, temp*2):
                if key[j][i] == 1:
                    key[j][i] = 0
                    key[j][i-1] = 1 
    elif value == 3:
        for i in range(temp, temp*2):
            for j in range(temp, temp*2):
                if key[j][i] == 1:
                    key[j][i] = 0
                    key[j-1][i] = 1 
    elif value == 4:
        for i in range(temp, temp*2):
            for j in range(temp, temp*2):
                if key[j][i] == 1:
                    key[j][i] = 0
                    key[j+1][i] = 1     
    return key

def _90rotate(key):
    N = len(m) 
    ret = [[0] * N for _ in range(N)] 

    for r in range(N): 
        for c in range(N): 
            ret[c][N-1-r] = m[r][c]
    return ret

def _270rotate(key):
    N = len(m) 
    ret = [[0] * N for _ in range(N)] 
    for r in range(N): 
        for c in range(N): 
            ret[N-1-c][r] = m[r][c] 
    return ret



print(solution(key, lock))