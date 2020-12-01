
progresses = [93,30,55]
speeds = [1,30,5]

def solution(progresses, speeds):
    ing = []
    ing = progresses
    answer =[]
    while len(ing)!=0:
        count = 0
        for i in range(len(ing)):
            ing[i] += speeds[i]
        if ing[0] >= 100:
            while True:
                if len(ing) > 0:
                    if ing[0] >= 100:
                       del ing[0]
                       del speeds[0]
                       count += 1
                    else:
                        answer.append(count)
                        break
                else:
                    answer.append(count)
                    break               
    return answer
print(solution(progresses, speeds))