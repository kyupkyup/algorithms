

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
count = 0

def solution(key, lock):
    length = len(lock)

    extended_lock = [[0 for i in range(length*3)] for i in range(length*3)]
    # 
    ans = [[0 for i in range(length*3)] for i in range(length*3)]
    for i in range(length):
        for j in range(length):
            extended_lock[length+j][length+i] = lock[j][i]
            ans[length+j][length+i] = lock[j][i]
            
            # 큰 자물쇠 부분
            # 자물쇠를 leng.
            # .th * 3 *2 만큼 만들어줌
      

    for rotation in range(4): # 90 도 
        key = _90rotate(key) # 90도 돌아간 열쇠
        for i in range(1, length * 2): # 오른쪽
            for j in range(1, length * 2): # 아래쪽
                for k in range(length): # lock 좌표 #열쇠 좌표
                    for m in range(lenght): #lock 좌표  열쇠 좌표
                        if check(extended_lock[j+m][i+k], key[m][k]) == True:
                            return True
    return False

def check(lock, key):

    lock_len = len(lock)
    key_len = len(key)

    for i in range( key_len):
        for j in range( key_len):
            if lock[key_len + j][key_len + i] + key[j][i] != 1:
                return False
    return True
    # 체크하는 함수 들어온 key 와 lock 을 더해서 해당 범위의 숫자가 모두 1이면 true 출력



def _90rotate(key, length, lock):
    N = len(key) 
    ret = [[0] * N for _ in range(N)] 

    for r in range(N): 
        for c in range(N): 
            ret[c][N-1-r] = key[r][c]
    return ret

