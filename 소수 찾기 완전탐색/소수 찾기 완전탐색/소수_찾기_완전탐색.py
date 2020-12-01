
from itertools import permutations

numbers = "17"

def solution(numbers):

    ansList = []
    num = list(numbers)
    for i in range(1, len(numbers)+1): # 1부터 7까지 순열조합
        permute = permutations(num, i) # list 튜플
        answer = list(permute)
        for j in answer:
            ans = ""
            for k in range(len(j)):
                ans += j[k]
            if prime(int(str(ans))):
                ansList.append(int(str(ans)))
    return len(list(set(ansList)))

def prime(num):
    if num != 1 and num != 0:
        for i in range(2, num):
            if num % i == 0:
                return False
    else:
        return False
    return True

print(solution(numbers))