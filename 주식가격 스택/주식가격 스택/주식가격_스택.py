
prices = [100, 91, 2, 1, 2,3,1,2,1,2,2]

def solution(prices):
    stack = []
    answer = []
    realAns = []
    for i in range(len(prices)):
        if i == 0:
            stack.append(prices[i])
            answer.append([0, True])
        else:
            temp = i
            while temp != 0 and stack:
                if prices[i] < stack[-1]:
                    if answer[temp-1][1] == True:
                        del stack[-1]
                        answer[temp-1][1] = False
                    else:
                        temp -= 1
                        continue
                else:
                    break
                temp -= 1
            answer.append([0, True])
            stack.append(prices[i])

        if i == len(prices)-1:
            for i in range(len(answer)):
                realAns.append(answer[i][0])
            return realAns
        else:
            for i in range(len(answer)):
                if answer[i][1] == True:
                    answer[i][0] += 1

        

print(solution(prices))