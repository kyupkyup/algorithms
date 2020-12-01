from itertools import permutations
n = 12
weak =[1, 5, 6, 10] 
dist =[1, 2, 3, 4]

def solution(n, weak, dist):

    length = len(weak)
    answer = len(dist) + 1
    for i in range(len(weak)):
        weak.append(weak[i]+ n)

    # start 지점 선정
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count - 1]

            for index in range(start, start + length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count - 1]
                
                
            answer = min(count, answer)
    if answer > len(dist):
        return -1
    return answer




print(solution(n, weak, dist))