from collections import deque
board = []

def solution(board):
    answer = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[j][i] != 0:
                answer.append(board[j][i])
                # dq 에 들어감
                for k in range(len(board)):
                    for m in range(len(board)):
                        
                        if board[m][k] == temp:
                            #아래 있는지 확인
                            if m+1 < len(board):
                                if board[m+1][k] == 0:
                                    answer.remove(board[j][i])
                            # 위에 있는지 확인
                            for l in range(m, 0, -1):
                                if board[l][k] != 0:
                                    continue
                                else:
                                    answer[]board[l][k]
                                    

                                    
                        
def check_square():
    # 직사각형인지 확인

print(solution(board))