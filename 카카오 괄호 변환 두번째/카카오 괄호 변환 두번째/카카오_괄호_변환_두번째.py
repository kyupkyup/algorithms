
s = "()))((()"

def solution(s):
    answer = []
    answer = recursive(s, answer)

    return answer


def recursive(s , answer): 
    countRight1 = 1 # 올바른 문자열인지, 균형잡힌 문자열인지 확인하는 변수
    countRight2 = 0
    countBalance1 = 1
    countBalance2 = 0
    if s == "":
        return s


    for i in range(1, len(s)):
        if s[0] == "(":   # "("  시작하면서 균형잡혔으면 올바른
            if s[i] == "(":
                countRight1 += 1
            elif s[i] == ")":
                countRight2 += 1
            if countRight1 == countRight2:
                # 올바른 문자열
                answer = s[:i+1]+ recursive(s[i+1:], answer)  
                #i 번째 까지 올바르다면 앞에꺼는 유지
                # 뒷부분은 재귀로 다시 균형인지 올바른인지 체크해줘야함
                return answer
        elif s[0] == ")":  # ")" 로 시작하면서 균형잡히면 그냥 균형잡힌
            #균형
            if s[i] == ")":
                countBalance1 += 1
            elif s[i] == "(":
                countBalance2 += 1
            if countBalance1 == countBalance2:
                #균형잡힌 문자열일 경우 앞 뒤에 "(",  ")"를 붙여주고 가운데 부분은 
                # v 재귀 시작 뒷부분은 "(", ")" 이 사이에 있던 내용을 뒤에 정렬해서 붙여줌
                # convert함수를 통해 따로 구현해줌 
                answer = "(" + recursive(s[i+1:], answer) + ")" + convert(s[1:i]) 

                return answer

def convert(s):
    ans = ""
    for j in range(len(s)):
        if s[j] == "(":
            ans += ")"
            continue
        elif s[j] == ")":
            ans += "("
            continue
    return ans
print(solution(s))