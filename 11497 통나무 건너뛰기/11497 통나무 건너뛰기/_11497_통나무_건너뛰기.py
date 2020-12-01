from itertools import permutations
t = int(input())
answer = []

def solution(n, arr):
    num = 0
    max_num = 10000000
    all_list = list(permutations(arr, len(arr)))

    for i in range(len(all_list)):
        if abs(all_list[i][0] - all_list[i][n-1]) > num:
            num = abs(all_list[i][0] - all_list[i][n-1])
        for j in range(1,n):
            if abs(all_list[i][j] - all_list[i][j-1]) > num:
                num = abs(all_list[i][j] - all_list[i][j-1])

            if num == 0:
                break

        if max_num > num:
            max_num = num
        num = 0
    return max_num

 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer.append(solution(n,arr))

for i in range(t):
    print(answer[i])