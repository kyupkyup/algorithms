
land = [[1, 100, 15, 3], [1, 2, 3, 4], [100, 99, 98, 97], [97, 98, 99, 100], [4, 3, 2, 1], [100, 100, 100, 100], [1, 1, 1, 1]]
answer = 0
def solution(land):
    global answer

#dp 
    sum = [0,0,0,0]
    pointer = 0
    dp(land, sum, pointer)
    return answer

def dp(land, sum, pointer):
    global answer
    next_sum = [0,0,0,0]
    
    if pointer == len(land):
        answer = max(sum)
        return 
    for i in range(4):
        next_sum[i] = max(land[pointer][i] + sum[(i+1)%4], land[pointer][i] + sum[(i+2)%4], land[pointer][i] + sum[(i+3)%4])
    dp(land, next_sum, pointer+1)
    return 
    
print(solution(land))