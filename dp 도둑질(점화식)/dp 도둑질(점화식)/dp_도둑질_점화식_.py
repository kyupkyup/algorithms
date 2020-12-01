
money = [1, 2, 3, 1]
def solution(money):
    money.insert(0, 0)
    result = []
    dp = [0 for i in range(len(money))]

    # 첫번째 집과 마지막집이 동시에 선택되면 안됨
    # 첫번째 집을 선택한 경우 마지막을 계산에서 빼주고
    # 두번째를 선택한 경우 첫번째를 뺴준다.

    # 첫번째 집 선택의 경우
    dp[1] = money[1]
    dp[2] = max(money[1], money[1])
    
    for i in range(3, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    result.append(dp[-2])

    #마지막집 선택의 경우
    dp = [0 for i in range(len(money))]
    dp[1] = 0
    dp[2] = money[2]
    for i in range(3, len(money)):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    result.append(dp[-1])

    return(max(result))
        

print(solution(money))