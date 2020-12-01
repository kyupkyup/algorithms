
heights = [1,5,3,6,7,6,5]


def solution(heights):
    stack = [0]
    answer = []

    for i in range(1, len(heights)+1):
        if i == 1:
            answer.append(stack[-1])
        else:
            if heights[i-2] > heights[i-1]:
                stack.append(heights[i-2])
                answer.append(i-1)
            elif heights[i-2] <= heights[i-1]:
                if stack[-1] > heights[i-1]:
                    answer.append(answer[-1])
                else:
                    answer.append(0)
    return answer
print(solution(heights))