#  그리디하게 풀 가장 최선의 방법을 먼저 찾아내야함!
#  이 문제에서는 앞 뒤 중 한명에게 밖에 체육복을 못 빌리는 사람에게 먼저 빌려주는 것
#  체육복을 못 앞 뒤 중 한 사람에게 빌릴 수 없는 사람부터 처리해준다면 가장 많은 사람이 체육을 할 수 있다고 기대하는 것
#


def solution(n, lost, reserve):
    answer= []
    for i in range(1, n+1):  # answer 리스트 생성
        answer.append(i)
    temp = []
    for i in lost:   # 잃어버린 사람 중에  
        if i in reserve:  # 체육복을 여벌로 가져온 사람 처리
            reserve.remove(i)
            temp.append(i)
    for i in temp:
        lost.remove(i)  # 체육을 할 수 있으므로 lost에서 삭제

    for i in lost:  # lost 인원 중 
        answer.remove(i)  # 일단 체육을 할 수 없다고 함
        if i+1 in reserve and i-1 not in reserve:  # 만약 앞에 체육복이 있고 뒤에는 없다면
            reserve.remove(i+1)  # 앞 사람을 reserve에서 삭제하고
            answer.append(i) #다시 체육을 할 수 있게 만듬
        elif i-1 in reserve and i+1 not in reserve: # 반대 상황
            reserve.remove(i-1)     
            answer.append(i)    
        elif i-1 in reserve or i+1 in reserve:  # 만약 둘 다 빌릴 수 있으면
            reserve.remove(i-1) # 앞사람껄 빌리도록 함
            answer.append(i)

    return len(answer)