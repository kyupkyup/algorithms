
N = 5
stages =	[2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    # 스테이지 = pointer 
    # i = 각 스테이지에서 막혀있는 사람
    answer = [] 
    ans = []
    for pointer in range(1, N+1):
        count_fail = 0  
        count_success = 0
        for i in stages: # 스테이지 순회
            if pointer == i:  # 포인터랑 같은 사람은 그 스테이지에서 머물러 있는 것이니 그 스테이지에서 실패한것
                count_fail += 1
            if pointer <= i:  # 포인터 보다 큰 사람은 그 스테이지를 성공
                count_success += 1 
        if count_success == 0:
            answer.append([pointer, 0]) # 성공한 사람이 없을 경우 0
        else:
            answer.append([pointer, count_fail/count_success]) # 각 스테이지에 실패한 사람과 성공한 사람을 나눠줌
    answer = sorted(answer, key=lambda x: (-x[1], x[0])) # 실패율이 같을 경우 스테이지가 작은 사람부터
    for i in answer:
        ans.append(i[0]) 
    return ans
print(solution(N, stages))