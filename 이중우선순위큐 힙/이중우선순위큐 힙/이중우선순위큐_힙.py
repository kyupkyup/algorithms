#
#  파이썬 list 의 : split [:1] 역할 알면 쉬움
#
#
operations = ["I 7","I 5","I -5","D -1"]

def solution(operations):

    list = [] # 큐 선언 리스트형태로  
    for i in operations:   # operations 를 순회하면서 모든 요소 검사
        if i[:1] == "I":    # 원소의 0번째 숫자가 I 라면 삽입 연산을 처리 하고
            list.append(int(i[1:]))
            # I 뒤에 나오는 모든 숫자를 정수형으로 변환해서 리스트에 추가
        elif i[:1] == "D":         # 원소의 0번째 글자가 D라면 삭제 => 1 과 -1 구분 필요
            if list:               # 리스트가 존재한다면 => 존재하지않으면 생략
                if i[2] == "1":    # i의 두번째 원소(띄어쓰기가 있으므로 1번째 원소는 생략) 가 1이라면 최대값 삭제 
                    list.remove(max(list))  # 최대값 삭제
                elif i[2:] == "-1":      # -1은 문자열이 두 개이기 때문에 2가 아니라 2: = 2뒤에 모든 원소까지 본다
                    list.remove(min(list))    # 최소값 삭제
    if not list:                            # 리스트가 없으면 [0, 0] 출력
        return [0,0]
    else:
        return [max(list), min(list)]       #리스트가 존재하면 [최대값, 최소값] 출력
print(solution(operations))