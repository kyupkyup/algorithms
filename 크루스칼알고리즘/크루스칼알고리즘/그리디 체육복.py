
#
# 그리디 알고리즘을 이용한 문제
# 가장 먼저 옷을 받아야 하는 친구들부터 받게 하는것이 핵심
# 
#
#


n = 5
lost = 	[3]	
reserve = 	[1]

def solution(n, lost, reserve):
    answer= []
    for i in range(1, n+1): # 학생 전체의 리스트 만들어줌(옷을 받지 못하는 lost를 여기서 빼주면 답)
        answer.append(i) 
    temp = []  #임시 리스트 (for 문을 돌리기 위한)
    for i in lost:  # 옷이 두 벌 있는 친구가 도둑맞는 경우 먼저 제외해야함
        if i in reserve:  # reserve 와 lost 가 같은 경우
            reserve.remove(i)  
            temp.append(i) #for 문의 기준이 lost이기 때문에 바로 빼주지 않고 temp 이용
    for i in temp:  # temp를 lost에서 빼줌
        lost.remove(i)

    for i in lost:   # 옷을 도난 당한 친구들에게 옷을 빌려주기 시작함
        answer.remove(i)
        if i+1 in reserve and i-1 not in reserve:  # 가장 우선 순위는 양쪽 중 한쪽에서만 받을 수 있는 경우
            reserve.remove(i+1) #위쪽
            answer.append(i)
        elif i-1 in reserve and i+1 not in reserve: # 아래쪽
            reserve.remove(i-1) 
            answer.append(i)    
        elif i-1 in reserve or i+1 in reserve: # 둘 다 받을 수 있는 경우
            reserve.remove(i-1)
            answer.append(i)

    return len(answer)

print(solution(n, lost, reserve))