import heapq

scovile = [1, 2, 3, 9, 10, 12]
K = 7

def solution(scoville, K):
    mix1 = 0
    mix2 = 0
    count=0
    heap = []
    for i in scovile:
        heapq.heappush(heap, i)
    while True:
        if heap[0] < K:
            mix1 = heap[0]
            heapq.heappop(heap)
            if not heap:
                return -1
            mix2 = heap[0]
            heapq.heappop(heap)
            heapq.heappush(heap, mix1 + mix2*2)
            count += 1
        else:
            break

    return count

print(solution(scovile, K))