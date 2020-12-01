import copy
baseball = [[321, 1, 1]]

def solution(baseball):
    num = [str(i) for i in range(111, 1000)]
    for i in num:
        for j in range(len(i)):
            if i[j] == "0":
                num.remove(i)
                break

    answer = []
    answer = copy.deepcopy(num)
    for play in baseball:
        if play[1] == 0 and play[2] == 0: # 아웃일 경우
            number = list(str(play[0]))
            for i in range(len(number)): # number
                for j in range(len(num)):
                    if number[i] == num[j][0] or number[i] == num[j][1] or number[i] ==num[j][2]:
                        if num[j] in answer:
                            answer.remove(num[j])
                        
        elif play[1] == 1 and play[2] == 0: # 1스트랔
            number = list(str(play[0]))
            for j in range(len(num)):
                if number[0] == num[j][0] or number[1] == num[j][1] or number[2] == num[j][2]:
                    continue
                else:
                    if num[j] in answer:
                        answer.remove(num[j])


        elif play[1] == 1 and play[2] == 1: # 1스트랔 1볼
            number = list(str(play[0]))
            for j in range(len(num)):
                for i in range(3):
                    temp = []
                    temp = copy.deepcopy(list(num[j]))
                    if (number[i] == num[j][i] and number[i-1] in list(temp.pop(i))) or (number[i] == num[j][i] and number[i-2] in list(temp)):
                        break
                    else:
                        if num[j] in answer:
                            answer.remove(num[j])

        elif play[1] == 2 and play[2] == 0: # 2스트랔 0볼
            number = list(str(play[0]))
            for j in range(len(num)):
                if (number[0] == num[j][0] and number[1] == num[j][1]) or ( number[1] == num[j][1] and number[2] == num[j][2])or (number[2] == num[j][2] and number[0]==num[j][0]):
                    continue
                else:
                    if num[j] in answer:
                        answer.remove(num[j])
        #elif play[1] == 2 and play[2] == 1: # 2스트랔 1볼


    print(answer)
solution(baseball)