
from collections import deque
N = 5
number = 3600
# NN
# N + N 
# N * N
# N - N
# N // N
#
def solution(N, number):
    answer = 0
    dq = deque([]) #큐 배열 선언 

    dq.append(N) #첫번째 숫자
    # n이 2면 [55, 10, 0, 25, 1]


    answer = numbering(dq, 2, N, number)

    return answer
    # dp 기존 배열에 넘버링을 해줘야함
               

def numbering(numList, count, N, number):
    
    if count > 8: # 8이 넘어가면 -1
        return -1

    next_list = deque([])  # 다음 dp에서 사용할 리스트 선언
    if number in numList:  # 현재 넘버 리스트에 맞는 숫자가 있으면 종료
        answer = count-1
        return answer
    temp = ""

    for i in range(count):  # N을 붙이는 경우
        temp += str(N)

    next_list.append(int(temp)) 
    while numList: 
        cal = numList.popleft() # 맨 앞 값을 소환

        next_list.append(cal + N) # 더한 값
        next_list.append(cal - N) # 뺸 값
        next_list.append(cal * N) # 곱
        if N != 0:
            next_list.append(cal // N)
        next_list.append(N - cal) # 나누기
        if cal !=0:
            next_list.append(N // cal)

    answer = numbering(next_list, count+1, N, number)
    return answer



def solution(N, number):
    arr = [set() for i in range(8)] # 각 카운트에서 계산된 목록
    
    for i, num in enumerate(arr, start=1): # 순서와 각 원소 지정
        num.add(int(str(N) * i))
    
    for i in range(1,len(arr)): # 1부터 8까지
        for j in range(i):  # 0부터 각 count까지
            for op1 in arr[j]: # 현재 지정된 카운트의 배열에 숫자
                for op2 in arr[i - j - 1]:  # 지금까지 카운트에 들어간 모든 배열의 숫자와 계산
                    arr[i].add(op1 + op2)
                    arr[i].add(op1 - op2)
                    arr[i].add(op1 * op2)
                    if op2 != 0:    
                        arr[i].add(op1 // op2)
        if number in arr[i]:
            answer = i+1
            break
    else:
        answer = -1
        
    return answer
print(solution(N,number))