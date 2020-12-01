
answer = []
m = 4
n = 5
board = 	["CCBDE", "AAADE", "AAABF", "CCBBF"]
def solution(m, n, board):
    # m은 높이, n은 폭
    # for 문을 순회하면서 해당 칸의 옆 아래 대각선 아래가 체크되는지 확인 
    # 확인 될 경우 true 리턴하면서 +1 해줌
    # 해당 블록들을 모두 0으로 만들어주고 
    # while 문이 돌아가고
    # 밑으로 부터 거꾸로 for문을 돌려서 특정 칸이 0이라면 그 위의 0의 개수 만큼 그 x값이 같은 위의 블록들의 y값을 더해주고 해당 칸을 그 블록으로 바꿈
    # 
    global answer
    result = 0
    while True:
        answer = []
        for j in range(m): # 높이부터
            for i in range(n): # 그 다음 길이
                if i <= n-2 and j<=m-2 and i>=0 and j>= 0:
                    if check(i, j, board):
                        result += 1

        board = change(n, m, board)
        print(board)
        break

def check(x, y, board):
    global answer
    if board[y][x] ==board[y+1][x] and board[y][x] == board[y+1][x] and board[y][x] == board[y+1][x+1]:
        answer.append([x,y])
        return True
    else:
        return False

def change(n, m, board):
    global answer
    new_board= []
    for j in range(m):
        cross =[]
        for i in range(n):
            if [i,j] in answer:
                cross.append("0")
            else:
                cross.append(board[j][i])
        new_board.append(cross)

    print(new_board)

    return new_board



solution(m,n,board)

