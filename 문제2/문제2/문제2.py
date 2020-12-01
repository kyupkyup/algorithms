from itertools import combinations
from collections import Counter 

orders =["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]

def solution(orders, course):
    answer = Counter()
    course_list = []
    maxlen = -1
    for order in orders:
        maxlen = max(len(order), maxlen)
        for i in course:
            course_list.append(list(map("".join, combinations(order, i))))
    new_course_list=[]
    word = []
    new_word= ""
    newnew=[]
    for course_li in course_list:
        for i in range(len(course_li)):
            word = sorted(course_li[i])
            new_word = "".join(word)
            new_course_list.append(new_word)
        newnew.append(new_course_list) 
        new_course_list=[]

    for course_li in newnew:
        answer += Counter(course_li)
    answer = answer.most_common()
    print(answer)
    temp = -1
    ans = []
    for cour in course:
        for i in answer:
            if len(i[0]) == cour:
                temp = max(temp, i[1])
        for i in answer:
            if len(i[0]) == cour and i[1] == temp and temp != 1:
                ans.append(i[0])

        temp=-1

    real_answer = []
    for i in ans:
        real_answer.append("".join(i))
    real_answer.sort()

    

    return real_answer

print(solution(orders, course))