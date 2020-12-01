N = int(input())
stairs = [0]
for i in range(N):
    stairs.append(int(input()))

ans = list()


def dp(N):
    if N == 1:
        ans.append(0)
        ans.append(stairs[1])
    elif N == 2:
        ans.append(0)
        ans.append(stairs[1])
        ans.append(stairs[1] + stairs[2])
    else:
        ans.append(0)
        ans.append(stairs[1])
        ans.append(stairs[1] + stairs[2])
        ans.append(max(stairs[2] + stairs[3], stairs[1] + stairs[3]))
    
        for i in range(4, N+1):
            ans.append(max(ans[i-2] + stairs[i], ans[i-3] + stairs[i]+ stairs[i-1]))
    print(ans[-1])
dp(N)