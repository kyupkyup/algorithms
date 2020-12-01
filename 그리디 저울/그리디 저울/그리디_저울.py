weight = [3, 1, 6, 2, 7, 30, 1]

def solution(weight):
    weight.sort()
    stack = []
    stack.append(weight[0])
    weight.remove(weight[0])
    
    temp = sum(stack)
    for weigh in weight:
        if weigh - temp > 1:
            return temp + 1
        else:
            temp += weigh
    return temp + 1

print(solution(weight))