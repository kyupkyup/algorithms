
N = int(input())

def fibo(n):
    ans = 0
    temp1 = 1
    temp2 = 2

    for i in range(1, n+1):
        if i == 1:
            ans = temp1
        elif i==2:
            ans = temp2
        else:
            ans = temp1 + temp2
            temp1 = temp2 % 15746
            temp2 = ans % 15746
    return ans

print(fibo(N)%15746)
