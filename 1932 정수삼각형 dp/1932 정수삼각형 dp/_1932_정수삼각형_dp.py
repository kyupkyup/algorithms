N = int(input())

num = [list(map(int, input().split(" "))) for i in range(N)]
ans = [[0 for j in range(N)] for i in range(N)]
def cal(N):
    pos = 0
    for i in range(N):
        if i == 0:
            ans[i][0] = num[i][0]
        else:
            for j in range(i+1):
                if j!=0 or j != i:
                    ans[i][j] = max(ans[i-1][j], ans[i-1][j-1]) + num[i][j]
                elif j==0:
                    ans[i][j] = ans[i-1][j] + num[i][j]
                elif j== i:
                    ans[i][j] = ans[i-1][j-1] + num[i][j]
    print(max(ans[-1]))
cal(N)