
N = int(input())
list = [N]
count = 0
def dp(answerList):
    returnList = []
    for i in answerList:
        returnList.append(i-1)
        if i%3 == 0:
            returnList.append(i/3)
        if i%2 == 0:
            returnList.append(i/2)
    return returnList

while True:
    if N == 1:
        print(count)
        break
    temp = dp(list)
    list = []
    list = temp[:]

    count += 1
    if min(list) == 1:
        print(count)
        break

