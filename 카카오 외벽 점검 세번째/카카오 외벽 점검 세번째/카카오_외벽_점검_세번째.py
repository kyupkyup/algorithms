import copy
from itertools import permutations
n = 12
weak=[1, 5, 6, 10]
dist = [1, 2, 3, 4]

def solution(n, weak, dist):

    # 원형 배열의 경우 배열의 길이를 두 배로 해서 직선으로 만든다
    # for 문을 순회해서 weak의 길이만큼 시작점을 정하고 weak의 길이만큼 순회한다.
    # 순회 한번마다 dist를 permutation 해서 몇번의 사람만에 그걸 충족하는지 판단
    # 
    answer = len(weak) + 1
    new_weak = copy.deepcopy(weak)
    for i in range(len(weak)):
        new_weak.append(weak[i] + n)

    for weak_point in range(len(weak)):
        for start in range(weak_point, len(weak)*2):
            for distance in list(permutations(dist, 3)):
                for i in distance:
                # 조건문
                # start 와 distance를 더한 값 사이에 new_weak 내에 몇개가 있는지? len(weak) 와 비교 
                # 비교해서 len(weak)가 더 작다면 바로 count 리턴
                # 더 크다면 다음 distance로 넘어가서 계산
                    temp = new_weak[start] + i # 친구가 한번에 이동하는 거리
                    for k in range(start, len(weak)):
                        if new_weak[k] < temp:
                            
                print(0)
solution(n, weak,dist)