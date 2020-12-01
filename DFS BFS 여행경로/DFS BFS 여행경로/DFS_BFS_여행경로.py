from collections import deque
#tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
tickets =[['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]

def dfs(stack, tickets):

    visited = []

    while len(visited) < len(tickets):
        list = []  
        start = stack[-1]
        check = False
        for ticket in tickets:
            if ticket[0] == start and ticket not in visited:
                list.append(ticket)

        if len(tickets) - len(visited) > 1:
            for part in list[:]:
                for ticket in tickets:
                    if part[1] == ticket[0]:
                        check = True
                        break
                if not check:
                    list.remove(part)            

        if len(list) > 1:
            temp = min(list)
            visited.append(temp)
            stack.append(temp[1])
        elif len(list) == 1:
            visited.append(list[0])
            stack.append(list[0][1])
    return stack



def solution(tickets):
    for i in range(len(tickets)):
        tickets[i].append([i])

    stack = []
    stack.append("ICN")
    answer = dfs(stack, tickets)
    return answer



print(solution(tickets))