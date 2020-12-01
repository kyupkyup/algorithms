
n = int(input())
apple_num = int(input())

apple = [list(map(int, input().split(" "))) for _ in range(apple_num)]
move_num = int(input())

move_snake = [list(input().split(" ")) for _ in range(move_num)]
answer = 0
snake =[[1,1]] 

def solution():
    global snake, answer
    direction = [1,2,3,4] # 오른쪽이 1 아래 2 왼 3 위 4
    current_direction = direction[0]

    for i in range(move_num): # move 전체 배열
        if i == 0:
            current_direction = move(current_direction, int(move_snake[i][0]), move_snake[i][1])
            if current_direction == None:
                return answer
        else:
            current_direction = move(current_direction, int(move_snake[i][0])-int(move_snake[i-1][0]), move_snake[i][1])
            if current_direction == None:
                return answer  

    move(current_direction, 100, "X")
    if current_direction == None:
        return answer  
    return answer

def move(direction, j, direc): 
    global answer, snake
    for i in range(j):
        if direction == 1:
            # 사과가 있다면
            # 벽이 있다면
            # 내 몸이라면
            #  다 아니라면

            if [snake[-1][0], snake[-1][1]+1] in apple:
                apple.remove([snake[-1][0], snake[-1][1]+1])
                snake.append([snake[-1][0], snake[-1][1]+1])
                answer += 1

            elif snake[-1][1]+1 > n:
                answer += 1
                return 
            elif [snake[-1][0], snake[-1][1]+1] in snake:
                answer += 1
                return 
            else :
                answer+=1
                snake.append([snake[-1][0], snake[-1][1]+1])
                snake.pop(0)
        elif direction == 2:
            if [snake[-1][0]+1, snake[-1][1]] in apple:
                apple.remove([snake[-1][0]+1, snake[-1][1]])
                snake.append([snake[-1][0]+1, snake[-1][1]])
                answer += 1

            elif snake[-1][0]+1 > n:
                answer += 1
                return 
            elif [snake[-1][0]+1, snake[-1][1]] in snake:
                answer += 1
                return 
            else :
                answer+=1
                snake.append([snake[-1][0]+1, snake[-1][1]])
                snake.pop(0)
        elif direction == 3:
            if [snake[-1][0], snake[-1][1]-1] in apple:
                apple.remove([snake[-1][0], snake[-1][1]-1])
                snake.append([snake[-1][0], snake[-1][1]-1])
                answer += 1

            elif snake[-1][1]-1 <= 0:
                answer += 1
                return 
            elif [snake[-1][0], snake[-1][1]-1] in snake:
                answer += 1
                return 
            else :
                answer+=1
                snake.append([snake[-1][0], snake[-1][1]-1])
                snake.pop(0)
        elif direction == 4:
            if [snake[-1][0]-1, snake[-1][1]] in apple:
                apple.remove([snake[-1][0]-1, snake[-1][1]])
                snake.append([snake[-1][0]-1, snake[-1][1]])
                answer += 1

            elif snake[-1][0]-1 <= 0:
                answer += 1
                return 
            elif [snake[-1][0]-1, snake[-1][1]] in snake:
                answer += 1
                return 
            else :
                answer+=1
                snake.append([snake[-1][0]-1, snake[-1][1]])
                snake.pop(0)      
    direction = rotate(direction, direc )
    return direction

def rotate(direction, direc):
    if direc == "D":
        direction += 1
        if direction > 4:
            direction = 1
        return direction
    elif direc == "L":
        direction -= 1
        if direction < 1:
            direction = 4
        return direction

print(solution())