from itertools import combinations
relation = [["a","1","4"],["2","1","5"],["a","2","4"]]
count = 0
def solution(relation):

    visited = [False for _ in range(len(relation[0])+1)]
    tuple = [i for i in range(1, len(relation[0])+1)]
    # 조합 한 개씩 해서 가능 한 것 제외
    # 조합 두 개씩 해서 가능 한 것 제외
    # 쭉쭉 relation 크기 까지
    for i in range(len(relation)):
        for j in range(len(relation[0])):
            #조합 제작
            break

    for k in range(1,len(relation[0])+1):
        for comb in list(combinations(tuple, k)):
            check(relation, comb, visited)
    return count
    # 해당 튜플로 모든 변수가 유일성을 띄는지 확인
def check(relation, comb, visited):
    #comb 첫빠따 1,2,3,46
    # 두번 1,2  1,3, 
    global count
    ans = []

        # comb 순회
    
    for j in range(len(relation)):
        answer = ""
        for i in range(len(comb)):
            if visited[comb[i]] == True:
                break            
                # 방문하지 않았었고, answer에도 들어가지 않았다면 
            answer += relation[j][comb[i]-1]

        if answer not in ans and answer !="":
            ans.append(answer)
    if len(ans) == len(relation):
        count += 1
        for i in comb:
            if visited[i] == False:
                visited[i] = True
    return
print(solution(relation))