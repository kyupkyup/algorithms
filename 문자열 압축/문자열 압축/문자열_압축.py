
#정답률 25.9
s="aabbaccc"

def solution(s):
    answer = ""
    answerList=  []
    for i in range(1, len(s)//2+1): # 1부터 s의 길이까지 한번씩 짤라서 같은게 있는지

        count = 1
        for j in range(0,len(s),i): # i 는 전체 i 몇 번 자르는지

            if s[j:j+i] == s[j+i : j+i+i]: # 자른 문자열과 그 다음 자른 문자열이 같은지
                count += 1 
            else:  # 다르면 지금까지 카운트 한 내용을 처리
                if count < 2:  # 카운트가 0이나 1이면 따로 입력 안해주므로
                    answer = answer + s[j:j+i]   # 바로 문자열로 붙여주고
                else:
                    answer = answer + str(count) + s[j:j+i]   # 2이상이면 숫자를 넣어줌
                count = 1 #카운트 초기화
        print(answer)
        answerList.append(len(answer))
        answer = ""
    return min(answerList)
solution(s)