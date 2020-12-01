
name = "ABAABAAAAAAAAAAAABAAAB"

def solution(name):
    answer = []
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
    
    for i in range(len(name)): # 각 name의 알파벳에 대하여 순회
        answer.append([name[i], False, 0])
        if answer[i][0] == "A":
            answer[i][1] = True
    i = 0
    ans = 0
    while True:
        if answer[i][1] == True:
            countF = 0
            countB = 0
            k = i
            m = i
            if answer[k+1][1] ==True and answer[m-1][1] == True:
                while countF == countB:
                    if answer[k+1][1] == True:
                        k += 1
                        countF += 1
                    
                    if answer[m-1][1] == True:
                        m -= 1
                        countB += 1
                if countB > countF:
                    i+=1
                    ans += 1
                elif countF > countB:
                    i-=1
                    ans += 1
            k = i
            m = i
            if answer[k+1][1] ==False and answer[m-1][1] == False:
                while countF == countB:
                    if answer[k+1][1] == False:
                        k += 1
                        countF += 1
                    
                    if answer[m-1][1] == False:
                        m -= 1
                        countB += 1
                if countB > countF:
                    i+=1
                    ans += 1
                elif countF > countB:
                    i-=1
                    ans += 1
            k = i
            m = i
            if answer[k+1][1] == True and answer[k-1][1] == False:
                i -= 1
                ans += 1
            k = i
            m = i
            if answer[k-1][1] == True and answer[k+1][1] == False:
                i += 1
                ans += 1
        else:
            if alphabet.index(answer[i][0]) > 13:
                answer[i][2] = 26 - alphabet.index(answer[i][0])
                answer[i][1] = True
            else:
                answer[i][2] = alphabet.index(answer[i][0])
                answer[i][1] = True
        count = 0
        for j in answer:
            if j[1] == False:
                break
            else: 
                count += 1
        if count >= len(answer):
            for i in answer:
                ans += i[2]
            return ans
        
                    
     
print(solution(name))