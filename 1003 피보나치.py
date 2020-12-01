import copy

T = int(input())
N = [int(input()) for i in range(T)]
count0 = [1,0]
count1 = [0,1]


def Fibo(num):
    length = len(count0)
    if length <= num:
        for i in range(length, num+1):
            count0.append(count0[i-2] + count0[i-1])
            count1.append(count1[i-2] + count1[i-1])
    print(count0[num], count1[num])

for i in range(T):
    Fibo(N[i])
