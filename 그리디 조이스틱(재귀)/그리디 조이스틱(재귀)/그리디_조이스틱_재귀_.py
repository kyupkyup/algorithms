
name = "JEROEN"
def solution(name):
    answer = []
    for i in range(len(name)): # 각 name의 알파벳에 대하여 순회
        answer.append([name[i], False, 0])
        if answer[i][0] == "A":
            answer[i][1] = True


    ans = []
    return movement(answer, 0, 0)        


def movement(answer, count, pointer):
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    ans = []

    while True:
        cnt = 0
        for i in answer:
            if i[1] == True:
                cnt += 1
        if len(answer) == cnt:
            return count
        else:

            if answer[pointer][1] == True:
                

            else:
                if alphabet.index(answer[pointer][0]) > 13:
                    count += 26 - alphabet.index(answer[pointer][0])
                    answer[pointer][1] = True
                else:
                    count += alphabet.index(answer[pointer][0])
                    answer[pointer][1] = True
print(solution(name))