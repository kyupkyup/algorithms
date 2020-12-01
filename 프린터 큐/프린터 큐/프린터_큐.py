
priorities = [2, 1, 3, 2]
location = 2
def solution(priorities, location):
    check = False
    answer = []

    while True:
        if len(priorities) == 0 :
            return location
            
        else:
            for i in range(1, len(priorities)):
                if priorities[0] < priorities[i]:
                    check = True
            if check == True:
                priorities.append(priorities[0])
                del priorities[0]
                if location > 0:
                    location -= 1
                else:
                    location += len(priorities) - 1
            else:
                answer.append(priorities[0])
                if location == 0:
                    location = len(answer)
                    return location
                del priorities[0]
                location -= 1
            check = False
print(solution(priorities, location))