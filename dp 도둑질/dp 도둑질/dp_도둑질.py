
money = [1,2,3,4,5,6,5,4,3,2,1,1,2,3,4,5]
result = []

def solution(money):

    money.append(money[0])

    # dp 나눠서 시작
    #맨 첫번째 원소에서 시작과 두 번쨰 원소에서 시작
    # 한번 뛸지 두번 뛸지 결정
    i = 0
    dp(money[0], 0)
    dp(money[1], 1)
    return max(result)
            
def dp(current, pointer):
    global result, money
    # current = 현재 메모 값
    # pointer = i  값 return 하기 위해서
    if pointer+3 >= len(money):
        result.append(current)
        return

    dp(current + money[pointer+2], pointer+2)
    dp(current + money[pointer+3], pointer+3)
    return

print(solution(money))