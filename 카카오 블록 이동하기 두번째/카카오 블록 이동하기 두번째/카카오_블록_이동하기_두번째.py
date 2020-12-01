from collections import deque
import copy
board =[[0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1], [0, 0, 1, 0, 0, 0, 0]]

def solution(board):
    state = [[1,1],[2,1]] # x값이 같으면 가로 상태 y 값이 같으면 세로 상태
    board_length = len(board)

    apend = [1 for i in range(len(board[0])+2)]

    for j in range(board_length):
        board[j].insert(0, 1)
        board[j].append(1)
    board.insert(0, apend)
    board.append(apend)
    
    dq = deque([])
    visit = []
    dq.append([state, 0])

    while dq:
        if not dq:
            return cost 
        state, cost = dq.popleft()

        if [board_length, board_length] in state: # 목적지인지 확인 
            #for i in range(len(visit)):
            #    print(visit[i])
            return cost

        if not state in visit:
            visit.append(state)
            dq = next_node(state, board, dq, cost+1)
    return cost

def next_node(state, board, dq, cost):

    # 할 수 있는 모든걸 dq에 넣어서 리턴
    # 세로 상태일 경우 : x 값이 같음
    if state[0][0] == state[1][0]:
        if board[state[0][1]][state[0][0]-1] == 0 and board[state[1][1]][state[1][0]-1] == 0:
            # 왼쪽 회전(아래축)
            dq.append([sorted([[state[0][0]-1, state[0][1]+1], state[1]], key=lambda x: (x[0], x[1])),cost])
             # 왼쪽 회전(윗축)   
            dq.append([sorted([state[0], [state[1][0] -1,state[1][1]-1]], key=lambda x: (x[0], x[1])), cost])
                # 왼쪽 이동
            dq.append([sorted([[state[0][0] - 1, state[0][1]],[state[1][0] - 1, state[1][1]]], key=lambda x: (x[0], x[1])), cost])        

    
        if board[state[0][1]][state[0][0]+1] == 0 and board[state[1][1]][state[1][0]+1] == 0:
                # 오른쪽 회전(아래축)
            dq.append([sorted([[state[0][0] +1, state[0][1] +1], state[1]], key=lambda x: (x[0], x[1])),  cost])
                # 오른쪽 회전(윗축)
            dq.append([sorted([state[0], [state[1][0]+1, state[1][1] -1]], key=lambda x: (x[0], x[1])),  cost])
                #오른쪽 이동
            dq.append([sorted([[state[0][0]+1, state[0][1]], [state[1][0] + 1, state[1][1]]], key=lambda x: (x[0], x[1])),  cost])        
        # 위쪽 이동,
        if board[state[0][1] - 1][state[0][0]] ==0:
            dq.append([sorted([[state[0][0], state[0][1] - 1], [state[1][0], state[1][1] -1]], key=lambda x: (x[0], x[1])),  cost])
        #아래쪽이동
        if board[state[1][1] + 1][state[1][0]] == 0:
            dq.append([sorted([[state[0][0], state[0][1] + 1], [state[1][0], state[1][1] + 1]], key=lambda x: (x[0], x[1])),  cost])
     # 왼쪽 이동
    # 위 이동
    # 아래 이동

    if state[0][1] == state[1][1]:
        # 위쪽으로
        if board[state[0][1]- 1][state[0][0] ] == 0 and board[state[1][1]- 1][state[1][0] ] == 0:
            #위쪽 회전(오른축)
            dq.append([sorted([[state[0][0]+1,state[0][1]-1],[state[1][0], state[1][1]]], key=lambda x: (x[0], x[1])),  cost])
            # 위쪽 회전(왼축)
            dq.append([sorted([[state[0][0], state[0][1]],[state[1][0] -1, state[1][1] -1]], key=lambda x: (x[0], x[1])), cost])
            # 위 이동
            dq.append([sorted([[state[0][0], state[0][1] - 1],[state[1][0], state[1][1] - 1]], key=lambda x: (x[0], x[1])),  cost])
        #아래쪽으로

        if board[state[0][1] + 1][state[0][0]] == 0 and board[state[1][1]+1][state[1][0]] == 0:
            # 아래쪽 회전(오른축)
            dq.append([sorted([[state[0][0] + 1, state[0][1] +1 ],[state[1][0], state[1][1]]], key=lambda x: (x[0], x[1])),  cost])
            # 아래쪽 회전(왼축)
            dq.append([sorted([[state[0][0], state[0][1]], [state[1][0]-1, state[1][1]+1]], key=lambda x: (x[0], x[1])),  cost])
            # 아래 이동
            dq.append([sorted([[state[0][0], state[0][1] + 1], [state[1][0], state[1][1]+1 ]], key=lambda x: (x[0], x[1])),  cost])
        #오른쪽으로
        if board[state[1][1]][state[1][0]+1] == 0:
            #오른쪾이동
            dq.append([sorted([[state[0][0]+1, state[0][1]],[state[1][0] + 1, state[1][1]]], key=lambda x: (x[0], x[1])),  cost])
        #왼쪽으로
        if board[state[0][1]][state[0][0]-1] == 0:
            #왼쪽이동
            dq.append([sorted([[state[0][0]-1, state[0][1]], [state[1][0] - 1, state[1][1]]], key=lambda x: (x[0], x[1])),  cost])

    return dq
print(solution(board)) 