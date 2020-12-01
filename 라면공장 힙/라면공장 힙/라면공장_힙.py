import heapq
stock = 20
dates= [4,7,8, 14, 24]
supplies = [10, 2, 3, 5, 10]
k = 30


# 힙을 이용한 해결
# dates 를 순회하면서 stock 을 넘는 dates가 나올때까지 => stock을 넘어가는 date가 나오면 무조건공급을 받아야함
# 
# 바로 넘어가는 경우는 for문 없이 바로 supply 받음
# 바로 date를 넘어가지 않는 경우는 순회 시작한 부분부터 공급을 받아야 하는 date까지 heap에 supply를 저장하고
# 가장 최대값을 stock에 더해줌.
# 

def solution(stock, dates, supplies, k):
    heap = [] # 힙 빈 배열 선언
    count = 0 # 공급받은 횟수 
    idx = 0
    while True: 
        if stock >= k: # stock이 k(밀가루 못받는 일수)를 넘어갈 때 까지 계속 공급받기
            return count
        else:
            for i in range(idx, len(dates)): # idx = 가장 마지막으로 공급받은 날짜부터 다음에 반드시 공급받아야하는 날짜까지
                if stock - dates[i] >= 0: # stock보다 dates가 더 클 때까지 재고가 0 이하로 떨어진다. 
                    heapq.heappush(heap, (-supplies[i], supplies[i])) # supply 내용 힙에 저장
                    print(heap)
                    idx = i + 1 # 다음 날짜로 
                else:
                    break
            stock += heapq.heappop(heap)[1] # 반드시 공급받아야 하는 날짜에 지금까지 저장된 힙 내용 중 가장 큰 값을 더해 줌
                            # [1] 은 힙 최대값 구하는 공식 -> 튜플을 이용하기 때문에 (우선순위, 값) 형식 중에 값만 가져옴
            count += 1   # 공급받은 횟수

print(solution(stock, dates, supplies, k))