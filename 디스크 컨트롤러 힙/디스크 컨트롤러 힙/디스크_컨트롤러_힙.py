import math
import heapq
jobs = [[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]
# 
# 핵심은 ☆대기시간이 현재까지 진행된 총 작업시간에서 각각의 job이 유입된 시간을 뺀 것이란것
# 또한 wait_list에서 수행시간이 가장 적은 순서대로 처리해야 가장 빠르게 작업을 끝낼 수 있단것
# 작업시간은 = 대기시간 + 수행시간
# 수행시간은 current[1]
# 
#
def solution(jobs):
    heap = []
    wait_list = []
    proceed_time = 0 
   for i in jobs:
        heapq.heappush(heap, i) # 힙으로 정렬
    
    current = heapq.heappop(heap) # 맨 처음에 할 작업
    answer = []
    Sum = current[1] + current[0] # 전체 작업시간 초기화 => 맨 처음 작업유입시간 + 그 작업을수행한 시간
    # Sum = last job finish time
    answer.append(current[1])
    while True:
        if not current: #현재 작업이 아예 비어있으면 break 
            break 
        else:
            for i in range(len(heap)): # jobs에 있는 작업들 중 마지막 작업이 끝나는 시간보다 이전에 들어온 job들을
                   #wait_list에 넣어주는 작업
                if heap[i][0] <= Sum:
                    wait_list.append(heap[i])   #
                    wait_list.sort(key=lambda x: x[1]) #wait_list 정렬 수행시간이 작은 순으로 정ㄹ렬
            for i in wait_list: # wait_list에 들어간 내용을 jobs에서 제거
                if i in heap:
                    heap.remove(i)

            if not heap and not wait_list: # 둘 다 비었으면 작업이 끝난거니 종료
                current = []
                break
            
            if wait_list: # wait_list에 작업이 있는 경우와 없는 경우로 나눠서 처리
                            # 있다면 쉬는 텀이 없음 = 쉬는 시간 계산 필요 X 
                current = wait_list[0] # 현재 작업으로 다음 작업을 넣어줌
                del wait_list[0] # 작업에 들어왔으므로 wait_list 에서 삭제
                Sum += current[1] # 작업 총 시간에 수행시간을 더해줌
                answer.append(Sum - current[0]) #작업 총 시간에서 작업이 시작된 시간을 빼면 대기시간과 수행시간 계산 가능
            else:
                current = heapq.heappop(heap) 
                if Sum > current[0]: 
                    Sum += current[1] # 수행시간만 더해줌 = 대기시간이 없다
                else: # 작업 총 시간보다 작업시작 시간이 뒤에 있는 경우 == 쉬는 시간이 있다.
                    Sum = current[0] + current[1] # 시작시간에 수행시간을 더해줌
                answer.append(current[1]) # 모든 수행시간 + 대기시간을 리스트에 넣어줌

    print(math.trunc(sum(answer)/len(answer))) # 평균 산출

solution(jobs)