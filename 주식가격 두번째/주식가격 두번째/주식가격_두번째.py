


prices=    [0] * len(prices) 
[0,0,0,0,0,0,0]

array[0]

def solution(prices):
    stack = []
    answer = [0 for _ in range(len(prices))]
    stack.append(0)

    for i in range(len(prices)-1):
        # 스택에 없을 경우 
        if not stack:
            stack.append(i)
        
        for j in stack:
            answer[j] += 1

        while stack:
            if prices[stack[-1]] > prices[i+1]:
            # 스택에는 인덱스 저장
                stack.pop()
            else:
                stack.append(i+1)
                break

    return answer

solution(prices)