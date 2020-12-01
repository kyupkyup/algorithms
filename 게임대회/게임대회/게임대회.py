n = 8
a= 6
b = 7
answer = 0
def solution(n, a, b):
    global answer
        
    if a>b:
        dfs(b, a, 0)
    elif a<b:
        dfs(a, b, 0)
    return answer+1

def dfs(a,b,count):
    global answer
    if a == b-1 and a%2 == 1 and b%2 == 0:
        answer = count
        return 
    else:
        if a%2 == 0:
            a/= 2
        elif a%2 == 1:
            a = (a+1) /2

        if b%2 == 0:
            b/= 2
        elif b%2 == 1:
            b = (b+1) /2

        dfs(a, b, count+1)
    return

print(solution(n, a, b))