
import copy
n = 12
weak=[1, 5, 6, 10]
dist =[1, 2, 3, 4]
def solution(n, weak, dist):

    # weak 부분을 순회
    # dist는 큰 것부터 weak를 더했을 때 n이 넘어가면 0 == n 부터
    # 0 보다 작아지면 +12
    # 양쪽 방향 모두 try
    #
    #

    temp_front = 0
    temp_back = 0
    answer = []
    for i in range(len(weak)):
        weak[i] = weak[i] - n//2
    
    weak_front = copy.deepcopy(weak)
    temp_weak_front = copy.deepcopy(weak)
    temp_weak_back = copy.deepcopy(weak)

    for point in weak[:]: # 뒤로
        # weak 순회

        count_back = 1
        for i in range(len(dist)-1, 0, -1):
            
            # dist를 뒤에서 부터 (긴 것부터)
            # front 로 갈 경우 temp_front 보다 작은 수는 제거
            # back 으로 갈 경우 temp_front 보다 큰 수는 제거
            # 뺄 경우 더한 값과 기존 값 비교
            temp_back = point + dist[i]
            for area in temp_weak_back[:]:
                if area <= temp_back and area >= point:
                    temp_weak_back.remove(area)
            count_back += 1
        answer.append(count_back)
    for point in weak_front[:]:
        # weak 순회
        count_front = 1
        for i in range(len(dist)-1, 0, -1):
            
            # dist를 뒤에서 부터 (긴 것부터)
            # front 로 갈 경우 temp_front 보다 작은 수는 제거
            # back 으로 갈 경우 temp_front 보다 큰 수는 제거
            temp_front = point - dist[i] # 뺄 경우 더한 값과 기존 값 비교
            for area in temp_weak_front[:]:
                if area >= temp_front and area <= point:
                    temp_weak_front.remove(area)
            count_front += 1
        answer.append(count_front)
    return min(answer)
print(solution(n, weak, dist))