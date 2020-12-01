
import math
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
    count1 = 0
    count2 = 0
    intersection = []
    union = []
    answer1 = 0
    answer2 = 0

    for i in range(len(str1_arr)):
        count1 = str2_arr.count(str1_arr[i]) # 첫번째 배열의 문자가 두번째 배열에서 몇 번 나오는지
        count2 = str1_arr.count(str1_arr[i]) # 첫번째 배열의 문자가 첫번째 배열에서 몇 번 나오는지
        intersection.append([str1_arr[i], min(count1, count2)])
        union.append([str1_arr[i], max(count1, count2)])

    for i in range(len(str2_arr)):
        count1 = str1_arr.count(str2_arr[i]) # 첫번째 배열의 문자가 두번째 배열에서 몇 번 나오는지
        count2 = str2_arr.count(str2_arr[i]) # 첫번째 배열의 문자가 첫번째 배열에서 몇 번 나오는지
        intersection.append([str2_arr[i], min(count1, count2)])
        union.append([str2_arr[i], max(count1, count2)])
    count1 = 0
    count2 = 0

    #for j in range(len(str2_arr)):
    #    check = True
    #    for k in union:
    #        if str2_arr[j] == k[0]:
    #            check = False
    #    if check == True:
    #        count2 = str2_arr.count(str2_arr[j]) # 두번째 배열의 문자가 두번째 배열에서 몇 번 나오는지
    #        union.append([str2_arr[j],  count2])     
            
    #for i in range(len(str1_arr)):
    #    check = True
    #    for k in union:
    #        if str1_arr[i] == k[0]:
    #            check = False
    #    if check == True:
    #        count2 = str1_arr.count(str1_arr[i]) # 두번째 배열의 문자가 두번째 배열에서 몇 번 나오는지
    #        union.append([str1_arr[i], count2])  

    for i in intersection:
        answer1 += i[1]
    for i in union:
        answer2 += i[1]
    print(union)
    return math.floor(answer1 / answer2 * 65536)

print(solution(str1, str2))