
from itertools import combinations
N, M = map(int, input().split(" "))
city = [list(map(int, input().split(" "))) for _ in range(N)]


def solution():

    # 현재 치킨집을 모두 리스트에 저장
    all_chicken = []

    for i in range(N): # 가로
        for j in range(N):  #세로
            if city[j][i] == 2:
                all_chicken.append([i,j])
    all_houses=[]
    for i in range(N): # 가로
        for j in range(N):  #세로
            if city[j][i] == 1:
                all_houses.append([i,j])

    comb = list(combinations(all_chicken, M))
    least_all_chicken = []
    for com in comb: # 모든 조합 순회하면서 최소 치킨거리 저장할 준비
        chicken_length = []

            #각 집에 대한 치킨집의 거리 계산
        for house in all_houses:
            each_house_least = []
            for i in com:
                each_house_least.append(abs(house[0]-i[0]) + abs(house[1] - i[1]))
            chicken_length.append(min(each_house_least))
        least_all_chicken.append(sum(chicken_length))
    return min(least_all_chicken)

print(solution())
