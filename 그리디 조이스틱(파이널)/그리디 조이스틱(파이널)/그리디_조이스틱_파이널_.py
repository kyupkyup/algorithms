
import copy
name = "BBAAAAAAAABB"
def solution(name):
    answer = []
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    crossCount = []
    
    for i in range(len(name)): # 각 name의 알파벳에 대하여 순회
        answer.append([name[i], False, 0])
        if answer[i][0] == "A":
            answer[i][1] = True

    
    print(greedy(answer, 0, 0))
    

def greedy(answer, pointer, crossCount):
    cnt = 0
    for i in range(len(answer)):
        if answer[i][1] == False:
            cnt += 1
    if cnt == 0:
        return crossCount


    answer[pointer][1] = True
    countF = 0
    countB = 0
    count = 0
    pointer1 = pointer
    pointer2 = pointer

    while True:
        if  len(answer) - count == 0:
            break

        pointer1 += 1
        if pointer1 >= len(answer):
            pointer1 = len(answer) - pointer1 
        if answer[pointer1][1] == True:
            countF += 1 # 더 가깝다는 뜻
        pointer2 -= 1
        if answer[pointer2][1] == True:
            countB += 1
        if countF != countB:
            break
        # 작은쪽으로 움직여야함
    if countF > countB: # 프론트로 움직이고
        greedy(answer, pointer + 1, crossCount + 1)
        
    elif countF < countB: # 백으로 움직이고
        greedy(answer, pointer - 1, crossCount + 1)
        
    elif countF == countB:
        print(1)
print(solution(name))