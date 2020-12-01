
T = int(input())

N = [int(input()) for i in range(T)]

def fibo(N):
    ans = 0
    temp1 = 1
    temp2 = 1
    temp3 = 1

    for i in range(1, N+1):
        if i == 1:
            ans = temp1

        elif i == 2:
            ans = temp2
        elif i == 3:
            ans = temp3
        else: 
            ans = temp2 + temp1
            temp1 = temp2
            temp2 = temp3
            temp3 = ans
            
    return ans
for i in range(T):
    print(fibo(N[i]))

