

from collections import deque
board =[[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
count = 0
def solution(board):
    state = [[1,1],[1,2]] # x값이 같으면 가로 상태 y 값이 같으면 세로 상태
    
    board_length = len(board)

    apend = [1 for i in range(len(board[0])+2)]

    for j in range(board_length):
        board[j].insert(0, 1)
        board[j].append(1)
    board.insert(0, apend)
    board.append(apend)
    # bfs 문제 
    # 현재 가로 상태인지, 세로 상태인지 확인하는 함수 필요(check_)
    # 가로상태일 경우 세로 이동과 가로 이동, 회전하는 부분이 달라짐
    # 가능한건 가로, 세로 이동
    # 
    
    dq= deque([])
    dq.append(state)
    count = bfs(dq, board)

    

def bfs(dq, board):
    global count
    state = dq.popleft()
    # 만약 끝에 도착했다면 리턴
    # 
    count += 1
    if state[1][0] == len(board) -2 and state[1][1] == len(board):
        return

    dq.append(rotate_clock(state, board))
    dq.append(rotate_unclock(state, board))
    dq.append(move_right(state, board))
    dq.append(move_left(state, board))    
    dq.append(move_up(state, board))
    dq.append(move_down(state, board))    
    
    bfs(dq, board)
    return 
      

def rotate_clock(state, board):
    #가로
    if state[0][0] == state[1][0]:
        if board[state[0][0]][state[0][1]-1] != 1 and board[state[1][0]][state[1][1]-1] != 1:
            state[0][0] = state[0][0] + 1
            state[0][1] = state[0][1] - 1 
        return sorted(state)
    #세로
    elif state[0][1] == state[1][1]:
        if board[state[0][0]+1][state[0][1]] != 1 and board[state[1][0]+1][state[1][1]] != 1:
            state[0][0] = state[0][0] + 1
            state[0][1] = state[0][1] + 1
        return sorted(state)

    # 세로 상태와 가로 상태 구분
    #회전 함수
    #회전이 가능하면 state 리턴
    # 불가능 하면 리턴 안함

def rotate_unclock(state, board):
    # 세로 상태 가로 상태 구분
    #가로
    if state[0][0] == state[1][0]:
        if board[state[0][0]][state[0][1]+1] != 1 and board[state[1][0]][state[1][1]+1] != 1:
            state[0][0] = state[0][0] + 1
            state[0][1] = state[0][1] + 1
        return sorted(state)
    elif state[0][1] == state[1][1]:
        if board[state[0][0]-1][state[0][1]] != 1 and board[state[1][0]-1][state[1][1]] != 1:
            state[0][0] = state[0][0] - 1
            state[0][1] = state[0][1] + 1
        return sorted(state)
#def move_left(state, board):
#     # 세로 상태 가로 상태 구분
#def move_right(state, board):
#     # 세로 상태 가로 상태 구분
#    # 이동 함수
#    # 이동 가능하면 state 리턴
#    # 불가능 하면 리턴 안함

#def move_up(state, board):

#def move_down(state, board):
print(solution(board))