x, y = map(int, input().split(" "))
arr = [list(input()) for i in range(y)]
count = 0
visited = [[False for i in range(x)] for i in range(y)]

def goNext(dy):
    global x, y, count
    state = False
    if(dy < y):
        piping(0, dy, state)
        goNext(dy+1)

    else:
        return
    #elif arr[dy+1][0] != "x" and visited[dy+1][0] !=True:
    #    piping(0, dy, count)

    #goNext(dy+1)

def piping(dx, dy, state):
    global x, y, count
    visited[dy][dx] = True
 
    if(dx + 1 >= x):
        count += 1
        state = True
        return

    if dy - 1 >= 0 and dy+1 < y:
        if arr[dy-1][dx+1] != "x" and visited[dy-1][dx+1] != True:
            piping(dx+1, dy-1, state)
            if state:
                return

        #오른쪽으로 이동
        elif arr[dy][dx+1] != "x" and visited[dy][dx+1] != True:
            piping(dx+1, dy, state)
            if state:
                return
        #오른쪽 위 대각선 으로 이동

        # 대각선오른쪽 아래로 이동

        elif arr[dy+1][dx+1] != "x" and visited[dy+1][dx+1] != True:
            piping(dx+1, dy+1, state)
            if state:
                return

goNext(0)
print(count)