arrangement="()(((()())(())()))(())"


def solution(arrangement):
    stack = []
    count = 0
    answer = 0
    for i in range(len(arrangement)):
        if arrangement[i] == "(":
            stack.append(i)
            count += 1
            answer += 1 
        elif arrangement[i] == ")":
            if i - stack[-1] <= 1:
                count -= 1
                del stack[-1]
                answer += len(stack)
                answer -= 1
            else:
                count -= 1
                del stack[-1]
    return answer            

print(solution(arrangement))



