

m="acbbcdc"
k ="abc"
def sol(m, k):

    stringM = list(m)
    stringK = list(k)
    stack=[]
    for i in range(len(m)):
            if not k:
                break

            if m[i] == k[0]:
                stack.append(i)
                k = k[1:]
    stack = sorted(stack, reverse=True)

    for i in stack:
        del stringM[i]


    return str(stringM)

sol(m,k)