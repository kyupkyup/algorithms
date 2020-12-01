import math

N = int(input())
a = list()
def solution(n):
    answer = 0
    
    
    for i in range(2, n+1):
        count = 0
        num = int(math.sqrt(i))
        for j in range(2, num):
            if i % j == 0:
                count += 1
                break
                    
        if count == 0:
            answer += 1
    return answer

print(solution(N))