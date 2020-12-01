
answers =[1,3,2,4,2]
def solution(answers):
    oneAns = [1,2,3,4,5]
    twoAns = [2,1,2,3,2,4,2,5]
    threeAns = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    
    for i in range(len(answers)):
        one = i% len(oneAns)
        two = i% len(twoAns)
        three = i% len(threeAns)
        if answers[i] == oneAns[one]:
            count[0] += 1
        if answers[i] == twoAns[two]:
            count[1] += 1
        if answers[i] == threeAns[three]:
            count[2] += 1
    m = max(count)
    return [i+1 for i, j in enumerate(count) if j == m]
    
print(solution(answers))