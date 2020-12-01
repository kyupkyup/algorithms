import copy
board = [[0,0,0,0,0,0,0,0,0,0]
,[3,3,3,0,0,0,0,0,0,0]
,[0,0,3,0,0,0,0,0,0,0]
,[0,0,2,0,0,0,0,0,0,0]
,[2,2,2,0,0,0,0,0,0,0]
,[1,0,0,4,4,4,0,0,0,0]
,[1,0,0,4,0,5,0,0,0,0]
,[1,1,0,0,0,5,5,5,0,0]
,[0,0,0,0,0,0,0,0,0,0]
,[0,0,0,0,0,0,0,0,0,0]];

def solution(board):
    length = len(board)
    block = []
    impossible_block = []

    #번호 최대값 필요
    num = -1
    # 모든 보드 순회해서 채우는게 불가능한 블록 서치 
    for i in range(length):
        for j in range(length):
            if board[j][i] != 0:
                block.append([i, j, board[j][i]])
            num = max(num, board[j][i])

    impossible_block = check(block, num)

    #[4, 5]
    while True:

        new_impos_block = copy.deepcopy(impossible_block)


        # 새로운 블록에 impossible 블록을 추가해서 넣어줌
        # 그 새로운 블록과 기존의 impossible 블록의 길이가 같으면 리턴
        x_array = []
        # impossible 블록의 x값과 block x 값이 같은 블록이 있으면 임파서블에 추가
        for i in range(len(block)): 
            for j in range(len(impossible_block)):
                if block[i][2] == impossible_block[j]: # 임파서블 블록임
                    x_array.append(block[i][0])

        for i in range(len(block)):
            for j in range(len(x_array)):
                if block[i][0] == x_array[j]:
                    new_impos_block.append(block[i][2])
        
        new_impos_block = list(set(new_impos_block))

        if len(new_impos_block) == len(impossible_block):
            break

        impossible_block = copy.deepcopy(new_impos_block)
                # 불가능한 블록 순회하면서 x 
    # 보드를 돌면서 숫자 발견
    # 배열과 숫자를 연결해서 한 배열에 넣어줌
    # 해당 숫자가 있는 배열을 모아서 check 함수에 넣어줌
        
    # 불가능한 블록들과 x값이 같은 블록이 있는 경우 불가능
    # 불가능한 블록
    # 불가능한 블록이 본인 위에 있는 경우 다시 불가능한 블록에 넣어줌
    # 새로운 블록이 들어가지 않을 경우 브레이크
    answer = 0
    for i in range(1,num+1):
        if i not in impossible_block:
            answer += 1
    return answer

def check(block, num):
    impossible_block = []
    # 배열의 제일 아래(y값이 제일 큰 배열이 두개나 세개일 경우 가능)
    # 한개일 경우 불가능 
    
    for i in range(1, num+1):
        y_array = []
        for j in range(len(block)):
            if i == block[j][2]:
                y_array.append(block[j][1])
        temp = max(y_array)
        cnt = y_array.count(temp)
        if cnt < 2:
            impossible_block.append(i)
    return impossible_block
print(solution(board))