
#23.1%

p = ")))))())))))))))))()))))))(((((((((((((()((((()((((("
answer = ""
def solution(p):

    answer = recursive(p)
    return answer


       
def recursive(p):
    global answer
    count = 0
    count1 = 0
    count2 = 0
    for i in range(len(p)):
    #올바른 문자열인지 확인

        if p[i] == "(":
            count1 += 1
        elif p[i] == ")":
            if count1 > 0:
                count2 += 1
        if count1 == count2 and count1 != 0 and count2 != 0:
            answer = p[:i+1] + recursive(p[i+1:])
            return answer
    # 올바른 문자열로 바꾸는 과정


    if p == "":
        return p
    else: # 균형잡힌 인데 올바른 으로 바꿔야되는 것
        count1=0
        count2=0
        for i in range(len(p)):
            if p[i] == "(":
                count1 += 1
            elif p[i] == ")":
                count2 += 1

            if count1 == count2:
                answer = recursive("(" + p[count1 : count1+count2-1] + p[1:count1] +")") + recursive(p[count1+count2:])
                return answer

print(solution(p))