numbers = [20, 200, 20] 

def solution(numbers):
    numList = []
    answer = ""
    for i in numbers:
        temp = str(i)
        if len(temp) == 1:
            temp = temp+temp[-1]+temp[-1]+temp[-1]
            numList.append(temp)
        elif len(temp) == 2:
            temp = temp + temp[0:2]
            numList.append(temp)
        elif len(temp) == 3:
            temp = temp + temp[0]
            numList.append(temp)
        else:
            numList.append(temp)
    numList = list(map(int, numList))
    

        answer = answer + str(numbers[numList.index(max(numList))])
        numList[numList.index(max(numList))] = -1
    if answer[0] == "0":
        return "0"
    return answer
print(solution(numbers))