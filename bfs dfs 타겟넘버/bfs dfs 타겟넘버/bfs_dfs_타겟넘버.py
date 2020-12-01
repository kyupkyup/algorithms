

#
# dfs bfs 문제 두 방식 모두 풀 수 있음 
#
#
numbers = [1, 1, 1, 1, 1]
target = 3
count = 0
def solution(numbers, target):
    global count

    dfs(0, numbers, target, 0)
    return count

def dfs(pointer, numbers, target, sum):
    global count
    if len(numbers) == pointer:   # 끝까지 탐색을 완료했는지?
        if sum == target:  # 끝까지 탐색한 후 결과가 나온다면 count 더하기
            count += 1
            return 
        else:
            return  #결과가 없으면 그냥 리턴
    dfs(pointer+1, numbers, target, sum+numbers[pointer])  # pointer만 증가시켜주고 합계 계산
    dfs(pointer+1, numbers, target, sum-numbers[pointer])   

print(solution(numbers, target))