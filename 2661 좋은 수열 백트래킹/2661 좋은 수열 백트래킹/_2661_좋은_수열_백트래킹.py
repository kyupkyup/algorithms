n = int(input())
s = []

def back(idx):
    global s
    for i in range(1, idx//2 + 1):
        if s[-i:] == s[-i*2:-i]:
            return -1
    
    if idx == n:
        for i in range(len(s)): print(s[i], end="")
        return 0

    for i in range(1,4):
        s.append(i)
        if back(idx+1) == 0:
           return 0
        s.pop()



back(0)
