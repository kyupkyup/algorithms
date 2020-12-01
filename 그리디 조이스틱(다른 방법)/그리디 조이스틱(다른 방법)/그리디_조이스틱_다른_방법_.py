import copy
name = "AZAAAZ"


#
#
# 그리디 하게 푸는건 가장 가까운 완성되지않은 문자부터 찾아가는 것
# BAAAAAAAAABBBBAAAAAA
# 
#
#
def solution(name):
    answer = []

    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    
    for i in range(len(name)): # 각 name의 알파벳에 대하여 순회
        answer.append([name[i], False])
        if answer[i][0] == "A":
            answer[i][1] = True  # A의 경우 이미 완성되있으므로 True 로 만들어줌
    count = 0
    tempAnswer = copy.deepcopy(answer)  # 오른쪽 순회 가로로 몇번움직이는지
    crossCount = []
    for eachWord in tempAnswer:   
        cnt = 0
        for i in range(len(tempAnswer)):
            if tempAnswer[i][1] == True:  # 만약 바꿔도 되지 않는 다면
                cnt += 1 
        if cnt == len(tempAnswer): # 모든 단어가 다 처리되었으면
            break
        eachWord[1] = True
        count += 1  # False인 개수
    crossCount.append(count)

    tempAnswer = copy.deepcopy(answer)   # 왼쪽 순회 하면서 가로로 몇번 움직이는지
    if tempAnswer[0][1] == False:
        tempAnswer[0][1] = True
    count = 1
    for eachWord in list(reversed(tempAnswer)): 
        cnt = 0

        for i in range(len(tempAnswer)):
            if tempAnswer[i][1] == True:
                cnt += 1
        if cnt == len(tempAnswer):
            break
        eachWord[1] = True
        count += 1
    crossCount.append(count)
    count = 0
    for i in range(len(answer)):     # 각각의 word에 대해서 위 아래로 몇번 움직여야 하는지
        if answer[i][1] == False:
            if alphabet.index(answer[i][0]) > 13:  # 13보다 크다면, 중간값이 13  아래로 움직이고
                count += 26 - alphabet.index(answer[i][0]) 
                answer[i][1] = True
            else:
                count += alphabet.index(answer[i][0])  # 13보다 작으면 위로 움직이고
                answer[i][1] = True
    return min(crossCount) + count -1 


print(solution(name))
