from collections import deque

t = int(input())
answer = []

def solution(n, arr):
    dq = deque()
    arr.sort()
    num = 0

    for i in range(n-1, -1, -1):
        if i%2 == 1:
            dq.append(arr[i])
        elif i%2 == 0:
            dq.appendleft(arr[i])


    if abs(dq[0] - dq[n-1]) > num:
        num = abs(dq[0] - dq[n-1])
    for j in range(1,n):
        if abs(dq[j] - dq[j-1]) > num:
            num = abs(dq[j] - dq[j-1])

        if num == 0:
            break    


    return num



for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer.append(solution(n,arr))

for i in range(t):
    print(answer[i])