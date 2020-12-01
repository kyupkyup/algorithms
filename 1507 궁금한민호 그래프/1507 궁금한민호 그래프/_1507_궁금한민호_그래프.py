N = int(input())
arr = [list(map(int, input().split(" "))) for i in range(N)]
noRoute = [[0 for i in range(20)] for i in range(20)]

def Floyd():
    global arr, noRoute
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0 or arr[i][k] or arr[j][k]:
                    continue
                elif arr[i][j] == arr[i][k] + arr[k][j]:
                    arr[i][j] = 0
                elif arr[i][j] > arr[i][k] + arr[k][j]:
                    print(-1)
                    return
Floyd()
result =0
for i in range(N):
    for j in range(N):
        result += arr[i][j]
print(result//2)