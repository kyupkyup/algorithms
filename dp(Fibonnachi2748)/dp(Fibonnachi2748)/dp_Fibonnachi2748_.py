N = int(input())

def Fibo(count, ans, next):
    if(count >= N):
        print(ans)
        return ans
    
    else:
        currNum = next
        next += ans
        
        Fibo(count+1, currNum, next)

Fibo(0, 0, 1)
