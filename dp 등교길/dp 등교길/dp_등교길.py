# 길 찾는 경우의 수 고등학교 때 풀었던거
#
#
m = 4
n = 3
puddles = [[2,2]]  

def solution(m, n , puddles):
    
    map = [[0 for i in range(m+1)]for i in range(n+1)]
    # i 는 가로, j는 세로 == j부터 나와야함
    for i in range(1, m+1):
        for j in range(1, n+1):   # N, M 까지 모든 경우의 수를 계산해줌 길찾기 문제
            if i == 1 and j == 1 : 
                map[j][i] = 1
                continue
            elif [i, j] in puddles:
                map[j][i] = 0
                
            else:
                map[j][i] += map[j-1][i]+ map[j][i-1]
    return map[j][i] % 1000000007

print(solution(m, n, puddles))