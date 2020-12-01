citations =[3, 0, 6, 1, 5]	

# 핵심은 정렬된 citations 의 인용횟수보다 남은 길이(지금 인덱스 이상으로 인용된 횟수)가 같거나 크면 for문을 계속 도는것
# 현재 최대 인용횟수가 남은 길이보다 크다면 H-index가 더 커질 가능성이 있다는 것.
# 즉, citations의 인용횟수가 citations 의 길이 - citations[i] 보다 크거나 같으면 
# 길이 - 인용인덱스 
#
# 

def solution(citations):

    citations.sort() #정렬  [0, 1, 4, 5, 6]
    l = len(citations) #길이 구하기
    for i in range(l):  # citations 순회
        if citations[i] < l - i: # l-i = 남은길이   #citations[i] 가 < citations[i] 이상으로 인용된 횟수 
            continue                # 작으면 계속 돌아라 커질때 까지 = 최대값을 찾아야되니깐
        elif citations[i] >= l - i: # 크거나 같아지는 순간 H-index의 최대값이 나옴 , 
                                    # 예를 들어 지금 예제에서는 4, 4가 되는 순간 h-index는 
            return l-i # h-index의 최대값은 length 남은 길이이거나, 이게 인용된 횟수랑 딱 맞는 경우
    return 0
    
print(solution(citations))
