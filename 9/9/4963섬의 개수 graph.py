

def Find(dx, dy, W, H):
    if(dx+1 > W):
        return
    if(dy+1 > H):
        return
    if(dx < 0):
        return
    if(dy < 0):
        return
    if(visited[dy][dx] == True):
        return
    else:
        visited[dy][dx] = True


    if dx - 1 >= 0:        
        if(sqr[dy][dx-1] == 1):
            Find(dx-1, dy, W, H)
    if dy+1 < H:
        if(sqr[dy+1][dx] == 1):
            Find(dx, dy+1, W, H)
    if dx+1 < W:
        if(sqr[dy][dx+1] == 1):
            Find(dx+1, dy, W, H)
    if dy-1 >= 0:
        if(sqr[dy-1][dx] == 1):
            Find(dx, dy-1, W, H)
    if dx+1 < W and dy-1 >= 0:
        if(sqr[dy-1][dx+1] == 1):
            Find(dx+1, dy-1, W, H)
    if dx+1 < W and dy+1 <H:
        if(sqr[dy+1][dx+1] == 1):
            Find(dx+1, dy+1, W, H)
    if dx-1 >= 0 and dy+1 <H:
        if(sqr[dy+1][dx-1] == 1 ):
            Find(dx-1, dy+1, W, H)
    if dx-1 >= 0 and dy-1 >= 0 :
        if(sqr[dy-1][dx-1] == 1):
            Find(dx-1, dy-1, W, H)
    
def FindIsland(W, H): #sqr[y열][x행] W 가로 H 세로
    count = 0
    for i in range(H):
        for j in range(W):
            if visited[i][j] == False and sqr[i][j] == 1:
                Find(j, i, W, H)    
                count += 1
    return count

count = list()
while 1:
    W=0
    H=0
    W, H = map(int, input().split(" "))
    sqr = [list(map(int, input().split(" "))) for i in range(H) ]
    visited = [[False for i in range(W)] for j in range(H)]
    if(W == 0 and H ==0 ):
        break
    count.append(FindIsland(W, H))
for i in range(len(count)):
    print(count[i])