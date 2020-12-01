gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
def solution(gems):
    visited = []
    answer= {}
    gem_list = []
    ans = []
    for i in range(len(gems)):
        if gems[i] not in gem_list:
            gem_list.append(gems[i])
    
    for i in range(len(gems)):
        if gems[i] not in visited:
            visited.append(gems[i])
            answer[gems[i]] = i
        else:
            if len(visited) == len(gem_list):
                break
            else:
                answer[gems[i]] = i
    for value in answer.values():
        ans.append(value)
    return [min(ans)+1, max(ans)+1]

print(solution(gems))