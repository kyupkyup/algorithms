
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
count = 0

def solution(key, lock):
    global count
    length = len(key)
    extended_key = [[0 for i in range(length*3)] for i in range(length*3)]

    for i in range(length):
        for j in range(length):
            extended_key[length+j][length+i] = key[j][i]
            if lock[j][i] == 0:
                count += 1


    ans = bfs(extended_key, length, lock)
    return ans

def bfs(key, length, lock):
    ans = False

    # 회전하는 함수
    # 회전, 체크 4번 반복 후 이동
    ans = _90rotate(key, length, lock)
    if ans:
        return ans
    ans = _90rotate(key, length, lock)
    if ans:
        return ans
    ans = _90rotate(key, length, lock)
    if ans:
        return ans
    ans = _90rotate(key, length, lock)
    if ans:
        return ans
  

    #for i in range(length):
    #    for j in range(length):
    #        key[length + j-1][length*2 -i + 1-1] = key[length + j-1][length*2 - i-1] # 오른쪽으로 이동
    #bfs(key, length, lock)
    #for i in range( length):
    #    for j in range( length):
    #        key[length + j-1][length + i-1] = key[length + j-1][length + i + 1-1] # 왼쪽으로 이동
    #bfs(key,length, lock)
    #for i in range( length):
    #    for j in range( length):
    #        key[length+ j-1][length + i-1] = key[length + j + 1-1][length + i-1] # 위쪽으로 이동
    #bfs(key,length, lock)
    #for i in range( length):
    #    for j in range( length):
    #        key[length*2 - j + 1-1][length + i-1] = key[length*2 - j-1][length + i-1] # 아래쪽으로 이동
    #bfs(key,length, lock)


def check(key, length, lock):
    global count
    cnt = 0
    for i in range(length):
        for j in range(length):
            if lock[j][i] == 0 and key[j + length][i + length] == 1:
                cnt += 1
    if count == cnt:
        return True
    else:
        return False


def _90rotate(key, length, lock):
    N = len(key) 
    ret = [[0] * N for _ in range(N)] 

    for r in range(N): 
        for c in range(N): 
            key[c][N-1-r] = key[r][c]
    return check(key, length, lock)

print(solution(key, lock))