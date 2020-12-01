
N = int(input())

house = [list(map(int, input().split(" "))) for i in range(N)]
ans = [[0 for i in range(3)] for j in range(N)]
def paint(N):

    for i in range(N):
        for j in range(3):
            if i == 0:
               ans[i][j] = house[i][j]
           
            else:
                ans[i][j] = min(ans[i-1][(j+1)%3],ans[i-1][(j+2) %3]) + house[i][j]
    print(min(ans[-1]))
paint(N)

