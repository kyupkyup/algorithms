
import math
from collections import Counter

str1="shake hands"
str2 ="handshake"
def solution(str1, str2):
    # str1 str2 를 모드 두 글자씩 쪼개서 배열에 넣어주고 
    # 특수문자가 포함된 문자열 삭제
    # 모두 소문자로 만들어줌
    # 두 배열을 모두 순회하면서 해당 문자가 각각 배열에서 몇개씩있는지 카운트 해준후
    # minimum은 교집합에 카운트한 개수 만큼 넣어주고
    # maximum은 합집합에 카운트한 개수 만큼 넣어줌
    str1 = str1.lower()
    str2 = str2.lower()

    str1_arr = []
    str2_arr = []
    for i in range(len(str1)-1):
        str1_arr.append(str1[i] + str1[i+1])
    for i in range(len(str2)-1):
        str2_arr.append(str2[i] + str2[i+1])

    for word in str1_arr[:]:
        if not word.isalpha():
            str1_arr.remove(word)
    for word in str2_arr[:]:
        if not word.isalpha():
            str2_arr.remove(word)
    if len(str1_arr) == 0 and len(str2_arr)==0:
        return 65536

    counter1 = Counter(str1_arr)
    counter2 = Counter(str2_arr)

    intersection = counter1 & counter2

    union = counter1 | counter2
    print(intersection)
    print(union)
    return math.floor(sum(list(intersection.values())) / sum(list(union.values())) * 65536)
solution(str1, str2)