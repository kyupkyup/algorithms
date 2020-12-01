
from itertools import permutations

n = 12
weak = [1, 3, 4, 9, 10]
dist = 	[3, 5, 7]

def solution(n, weak, dist):
    
    weak_length = len(weak) # 중복으로 weak의 길이를 사용할 일이 많아서 미리 연산
    answer = len(dist) + 1 # 친구의 최소값을 찾기 위해서 

    for i in range(weak_length):
        weak.append(weak[i] + n)
    #원형을 직선으로 만들어주는 과정

    #1. weak 배열을 처음부터 끝까지 순회
    for i in range(weak_length):
        # 2. 친구들을 차례대로 배치하는 순열을 만들어줌 []
        # [3, 5, 7] 
        # [3, 7, 5]
        # [5, 7, 3]
        #

        for friends_list in list(permutations(dist, len(dist))):
            count = 1
            # 3. 첫번째 친구
            position = weak[i] + friends_list[count - 1]
            # 첫번째 친구가 들어가서 어디까지 돌 수 있는가? = position의 값
            for index in range(i, i + weak_length):
                # 4. 처음 들어가서 모든 친구들을 다 쓸 때까지 돈다. 
                if position < weak[index]: # 친구가 점검을 마치는 부분 = index가 친구가 점검하기까지의 부분
                    count += 1 #다음 친구 투입
                    if count > len(dist): # 친구를 다 투입했으면
                        break # 실패
                    position = weak[index] + friends_list[count-1] # 다음 친구는 전 친구가 마지막으로 점검했던 부분부터 다시 
                                                                   # 자기가 점검할 수 있는 부분까지 점검
            answer = min(answer, count) # 기존의 최소값보다 더 작은 값이 있다면 answer에 넣어줌
    if answer > len(dist): # 모든 처리 후에 나온 값이 친구를 다 쓴 것보다 크다면 모든 친구를 투입해도 모든 점검이 불가능하니
        return -1 # -1 리턴
    return answer



print(solution(n, weak, dist))