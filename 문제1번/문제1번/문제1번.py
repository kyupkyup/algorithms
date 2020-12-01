

new_id = 		"abcdefghijklmn.p"
def solution(new_id):
    # 모든 대문자 -> 소문자
    
    temp1 =""

    for word in new_id:
        if word.isupper() == True:
            temp1 += word.lower()
        else:
            temp1 += word
                # 알파벳, 숫자, -, _, . 뺴고 삭제

    temp2 = ""
    for word in temp1:
        if word.isalpha() == True or word.isdigit() == True or word=="-" or word =="_" or word == ".":
            temp2 += word
                # .가 중복될 경우 하나로 바꿈
    count = 0
    temp3 = ""
    j = 0 
    while j < len(temp2):
        for i in range(j, len(temp2)-1):
            if temp2[i] == "." and temp2[i+1] == ".":
                count += 1
            else:
                break
        if count > 0:
            temp3 += temp2[j+count]
            j = j + count+1
            count = 0
        else:
            temp3 += temp2[j]
            count = 0
            j += 1    

        
    temp4 = ""

    # 마침표 처음 끝일 경우 삭제
    
    if len(temp3) != 0:
        if temp3[0] == ".":
            temp3 = temp3[1:]
    if len(temp3) != 0:
        if temp3[-1] == ".":
            temp3 = temp3[:-1]
    # 빈문자열일경우 a
    if len(temp3) == 0:
        temp3 += "a"


    temp4 = temp3[:15]
    if temp4[-1] == ".":
        temp4 = temp4[:-1]
    
    if len(temp4) <= 2:
        while len(temp4) < 3:
            temp4 += temp4[-1]



    return temp4

print(solution(new_id))