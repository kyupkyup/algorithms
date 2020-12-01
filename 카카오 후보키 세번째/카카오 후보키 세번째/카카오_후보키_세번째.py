from itertools import combinations

relation =[["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):

    column_length = len(relation[0]) # 컬럼 순회를 위한 길이 미리 선언
    row_length = len(relation) # 행순회를 위한 길이 선언
    comb = [i for i in range(1, column_length+1)]  # 후보키 조합을 위한 콤비네이션 배열

    unique_list = []
    answer_list= []
    # 유일성 체크

    for j in comb:  # 콤비네이션을 순회하면서 모든 조합의 유일성을 찾아냄
        for combi_list in list(combinations(comb, j)): #[1] [2]  [1,2] [2,3]~~[1,2,3,4]
            unique_list.append(unique_check(relation, combi_list, unique_list))

    # 최소성 체크 - 부분 집합이용
    # 어떤 집합의 부분집합이 해당 집합에 존재하면 삭제
    
    for subset in unique_list: # 유일성을 만족하는 조합 중
        if subset == None:   # RETURN 값에 none 이 있을 경우 패스
            continue
        subset = set(list(subset))  # 집합 형태로 만들어줌 set() => 리스트 집합 [1,1,1,3,4]  [1,3,4]
        check = True  
        # 부분 집합인지 검사합니다.
        for j in answer_list:  # 답에 넣어놓은 부분집합이 다른 집합의 부분집합이 되는 경우를 탐색
            if j.issubset(subset): # set(A).issubset(B) # A가 B의 부분 집합인지 검사
                check = False # 어떤 집합의 부분집합이 존재한다면 그 부분집합이 최소성을 만족하는 집합이므로 그 내용만 answer_list에 넣어줌
        if check == True:
            answer_list.append(subset) 

    return len(answer_list)

def unique_check(relation, combi_list, unique_list):
    column_length = len(relation[0]) #[1] [2] [3] + [1,2][1,3]
    row_length = len(relation)

    temp_list = []
    for i in range(row_length): # 행을 돌면서 모든 값이 중복되지 않는지 중복되는지 확인 
        temp = ""
        for j in combi_list:
            temp += relation[i][j-1]  #temp ="apeachmath" [1], [2,3]  
        if temp not in temp_list:  
            temp_list.append(temp)

    if len(temp_list) == row_length: # 중복된다면 새롭게 만들어진 배열이 기존 배열과 길이가 다를 것이니
        return combi_list # 그때 콤비리스트를 리턴
    return # 중복되지 않는 경우 NONE 리턴

print(solution(relation))