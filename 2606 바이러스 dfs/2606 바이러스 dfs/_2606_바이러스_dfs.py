
N = int(input())
M = int(input())

matrix = [[0] * (N + 1) for _ in range(N+1)]
for _ in range(M):
    route = list(map(int, input().split(" ")))
    matrix[route[0]][route[1]] = 1
    matrix[route[1]][route[0]] = 1

def dfs(current_node, matrix, visit):
    visit += [current_node]
    for search_node in range(len(matrix[current_node])):
        if matrix[current_node][search_node] and search_node not in visit:
            visit = dfs(search_node, matrix, visit)
    return(visit)
    

print(len(dfs(1, matrix, []))-1)