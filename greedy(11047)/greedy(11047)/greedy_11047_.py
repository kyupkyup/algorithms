
inpu = input().split(" ")

arr = [0 for i in range(int(inpu[0]))]
for i in range(int(inpu[0])):
    arr[i] = int(input())
ans = int(inpu[1])


middleans = 0 
count = 0
for i in range(int(inpu[0])-1, -1, -1):
    if(middleans == ans):
        break
    while 1:
        if(arr[i] + middleans <= ans):
            count = count + 1
            middleans = middleans + arr[i]
        else:
            break
print(count)

N, ans = map(int, input().split(" "))
arr = [int(input()) for i in range(N)]
middleAns = 0
count = 0


for i in range(N-1, -1, -1):
    if(ans >= arr[i]):
        middleAns = ans // arr[i]
        ans -= middleAns * arr[i]
        count += middleAns
print(count)

#N, K = map(int, input().split())
#coins = [int(input()) for _ in range(N)] 

## 최소 동전 개수 구하기 
#coin_num = 0

#for i in range(1,N+1):
#    # 인덱스 끝부터 순회 : 마이너스 인덱스 
#    coin = coins[-i]
    
#    if K >= coin : 
#        num = K//coin
#        K -= coin*num
#        coin_num += num
        
#print(coin_num)