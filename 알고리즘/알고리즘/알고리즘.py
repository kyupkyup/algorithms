import copy

inpu = input().split(" ")
for i in range(len(inpu)):
  inpu[i] = int(inpu[i])

arr = ["" for i in range(inpu[0])]

for i in range(inpu[0]):
  arr[i] = input().split(" ")

for i in range(inpu[0]):
  for j in range(inpu[1]):
    arr[i][j] = int(arr[i][j])
Visited = [[False for i in range(inpu[0])] for i in range(inpu[1])]
ans = []

def Roller(arr):
# 경우의 수 계산 하는 함수
# 가로가 홀수인 경우, 세로는 상관 없음 => 모두 탐색 가능
# 세로가 홀수인 경우, 가로는 상관 없음 => 모두 탐색 가능
# 둘 다 짝수인 경우, 

    global Visited
    EvenNumCountArr = [0 for i in range(inpu[0])]
    EvenNumCount = 0
    if(inpu[0]%2==1 and inpu[1]%2==1):
        MoveDown(Visited)
    elif(inpu[0]%2==1 and inpu[1] % 2 !=1): #세로 개수 홀수 가로로 움직임
        MoveCross(Visited)
    elif(inpu[1]%2==1 and inpu[0] % 2 != 1): # 가로 개수 홀수 세로로 움직임
        MoveDown(Visited)
    else:
        #둘 다 짝수 인 경우 한개를 방문하지 못한다. 가장 작은 수 골라서 Visited처리
        for i in range(inpu[0]):
            EvenNumCountArr[i] = min(arr[i])
        EvenNumCount = min(EvenNumCountArr)
        for i in range(inpu[0]):
            for j in range(inpu[1]):
                if(arr[i][j] == EvenNumCount):
                    Visited[i][j] = True
        MoveThird(Visited)

def MoveCross(VisitedFirst):
    global inpu
    currentPos = [0,0]
    Visited = copy.deepcopy(VisitedFirst)
    Visited[0][0] = True
    while 1:
        if(currentPos[0] == inpu[0]-1 and currentPos[1] == inpu[1] -1):# 끝에 도착할 경우
            if False in Visited:
                currentPos[0] = 0
                currentPos[1] = 0
                Visited = copy.deepCopy(VisitedFirst)
                Visited[0][0] = True
            else:
                return               

        if(currentPos[1] == 0):
            if(Visited[currentPos[0]][currentPos[1] + 1]  == True):
                print("D")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[0] = currentPos[0] + 1
            elif(Visited[currentPos[0]][currentPos[1] + 1]  == False):
                print("R")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[1] = currentPos[1] + 1
        elif(currentPos[1] == inpu[1] - 1):
            if(Visited[currentPos[0]][currentPos[1] - 1]  == True):
                print("D")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[0] = currentPos[0] + 1
            elif(Visited[currentPos[0]][currentPos[1] - 1]  == False):
                print("L")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[1] = currentPos[1] - 1
        else:        
            if(Visited[currentPos[0]][currentPos[1] - 1] == True):
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[1] = currentPos[1] + 1
                print("R")
            elif(Visited[currentPos[0]][currentPos[1] + 1] == True):
                Visited[currentPos[0]][currentPos[1]]= True
                currentPos[1] = currentPos[1] - 1
                print("L")

def MoveDown(VisitedFirst):
    global inpu
    currentPos = [0,0]
    Visited = copy.deepcopy(VisitedFirst)
    Visited[0][0] = True
    while 1:
        if(currentPos[0] == inpu[0]-1 and currentPos[1] == inpu[1] -1):# 끝에 도착할 경우
            if False in Visited:
                currentPos[0] = 0
                currentPos[1] = 0
                Visited = copy.deepCopy(VisitedFirst)
                Visited[0][0] = True
            else:
                return

        if(currentPos[0] == 0):
            if(Visited[currentPos[0]+1][currentPos[1]]  == True):
                print("R")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[1] = currentPos[1] + 1
            elif(Visited[currentPos[0]+1][currentPos[1]]  == False):
                print("D")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[0] = currentPos[0] + 1
        elif(currentPos[0] == inpu[0] - 1):
            if(Visited[currentPos[0]-1][currentPos[1]]  == True):
                print("R")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[1] = currentPos[1] + 1
            elif(Visited[currentPos[0]-1][currentPos[1]]  == False):
                print("U")
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[0] = currentPos[0] - 1
        else:        
            if(Visited[currentPos[0]-1][currentPos[1]] == True):
                Visited[currentPos[0]][currentPos[1]] = True
                currentPos[0] = currentPos[0] + 1
                print("D")
            elif(Visited[currentPos[0]+1][currentPos[1]] == True):
                Visited[currentPos[0]][currentPos[1]]= True
                currentPos[0] = currentPos[0] - 1
                print("U")

#def MoveThird(VisitedFirst):
#    #실제로 이동하는 함수(가로세로 짝수)
#    global ans
#    currentPos = [0,0]
#    Visited = copy.deepcopy(VisitedFirst)
#    Visited[0][0] = True
#    while 1:
        
#        if(currentPos[0] == inpu[0]-1 and currentPos[1] == inpu[1] -1):# 끝에 도착할 경우
#            for i in range(inpu[0]):
#                for j in range(inpu[1]):
#                    if(Visited[i][j] == False):
#                        currentPos[0] = 0
#                        currentPos[1] = 0
#                        Visited = copy.deepCopy(VisitedFirst)
#                        Visited[0][0] = True
#                    else:
#                        break
      
#        #i는 1일 경우 오른쪽
#        # i = 2 아래쪽 i=3 은 왼쪽 i=    

#        count = 0
#        for i in range(4): #오른쪽 
#            if(i==0):
#                if(currentPos[1]+1 < inpu[1] -1 ):
#                    if(Visited[currentPos[0]][currentPos[1] + 1] == False):
#                        currentPos[1] = currentPos[1] + 1
#                        Visited[currentPos[0]][currentPos[1]+1] = True
#                        ans.append("R")
#            elif(i==1): #왼쪾
#                if(currentPos[1] - 1 >= 0 ):
#                    if(Visited[currentPos[0]][currentPos[1] - 1] == False):
#                        currentPos[1] = currentPos[1] - 1
#                        Visited[currentPos[0]][currentPos[1]-1]   = True                    
#                        ans.append("L")
#            elif(i==2): #아래
#                if(currentPos[0] + 1 < inpu[1] - 1 ):
#                    if(Visited[currentPos[0] + 1][currentPos[1]] == False):
#                        currentPos[0] = currentPos[0] + 1
#                        Visited[currentPos[0]+1][currentPos[1]] = True
#                        ans.append("D")
#            elif(i==3): #위
#                if(currentPos[0] - 1 >= 0 ):
#                    if(Visited[currentPos[0] - 1][currentPos[1]] == False):
#                        currentPos[0] = currentPos[0] - 1
#                        Visited[currentPos[0]-1][currentPos[1]+1] = True
#                        ans.append("U")
Roller(arr)
