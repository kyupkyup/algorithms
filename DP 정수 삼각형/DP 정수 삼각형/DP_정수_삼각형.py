
import copy
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


# 중요한건 다음 라인을 기준으로 최대값을 쌓아가야한다는것.
# 중복되는 계산들을 max 로 처리해주는 것
#
##

def solution(triangle):

    triangle.insert(0, [0]) # 계산의 편의를 위해 맨 앞에 배열 하나를 넣어줌
    maxList = []  # 최대값을 저장할 리스트

    for i in range(1, len(triangle)):  # 삼각형의 세로를 내려오는 for 문
        if i == 1:                # 첫번째 노드의 경우 그냥 추가
            maxList.append(triangle[i][0])
        else:
            newList = []          # 매 층 마다 새로운 값들을 저장해야 해서 리스트 추가
            for j in range(i):    # 한 층에서 계산 시작
                if j == 0:        # 각 층에서 맨 앞 노드와 
                    newList.append(maxList[0] + triangle[i][0])
                elif j == i-1:   # 맨 뒷 노드는 다르게 처리
                    newList.append(maxList[j-1] + triangle[i][j])
                else:            # 중간 노드는 중복값이 발생하므로 그 중에 최대값을 저장
                    newList.append(max(triangle[i][j] + maxList[j], triangle[i][j] + maxList[j-1]))
            maxList = copy.deepcopy(newList)  # 다음 층으로 갈 수 있게 maxList에 newList를 넣어줌

    return max(maxList)

print(solution(triangle))