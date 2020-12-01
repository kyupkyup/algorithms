from itertools import combinations
relation =[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
def solution(relation):
    column_len = len(relation[0])
    column = []
    for i in range(1, column_len+1):
        column.append(i)
    combination = []
    # 컬럼이 몇 개인지 확인 
    # 조합을 사용해서 1~ 컬럼의 개수까지 가능한 조합 모두 소환
    # 체크 함수에서 해당 조합의 내용의 값이 모두 다르다면 그 조합을 모든 현재 조합에서 제외
    for i in range(1, column_len+1):
        combination.append(list(combinations(column, i)))

    # 조합을 한번씩 체크해서 배열마다(한 개짜리, 두개짜리 쭉쭉ㅉ꾸)
    
    for comb in combination:
        check(comb, relation)


def check(combination, relation):
    check = []
    
    # 조합을 받아와서 내용 확인
            # relation  확인
    for i in range(len(combination)):
        for j in combination[i]:
            # 여기서 부터 relation 확인
            for line in relation:
                check.append(line[j-1]) 
            new_list = []
            for v in check:
                if v not in new_list:
                    new_list.append(v)
            if len(check) == len(new_list):
                # 중복되는 것이 있다면 
                comb_delete(combination, j)

def comb_delete(combination, delete_num):
    # 조합에서 해당 내용 삭제
    for comb in combination:
        print(comb)


    return
solution(relation)