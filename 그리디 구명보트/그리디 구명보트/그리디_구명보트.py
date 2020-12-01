
#
# 핵심은 지금 당장 최선의 방법을 선택했을 때, 이것이 전체의 가장 최선의 결과를 내는지 판단하는 것
#  여기에선 가장 무거운 사람을 태웠을 때, 한 명을 더 태울 수 있는가 없는가
#  보트는 두명을 무조건 태워야 최소하게 왔다갔다 한다.
#
people =[70, 50, 80]	
limit = 100

def solution(people, limit):
    people.sort()  # 무게 순으로 정렬
    count = 0
    i=0   # 첫번째 사람 (가장 가벼운 사람)
    j = len(people) - 1    #마지막 사람(가장 무거운 사람)
    while i <= j:    # 앞과 뒤에서 한명씩 태우려고 해봄
        if people[i] + people[j] <= limit:  # 맨 뒤사람과 맨 앞 사람을 태웠을 때 limit을 넘지 않는 다면 2명을 태우는 것이기 때문에 최선
            count += 1  
            i += 1
            j -= 1
        else:  # limit가 넘어가버리면 맨 뒷사람만 태운다.
            count += 1
            j -= 1  # 맨 뒷사람만 태웠다

    return count
print(solution(people,limit))