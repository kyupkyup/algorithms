
N, M, V = map(int, input().split(" "))

matrix = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    route = list(map(int, input().split(" ")))
    matrix[route[0]][route[1]] = 1    
    matrix[route[1]][route[0]] = 1

def dfs(current_node, matrix, visit):
    visit += [current_node]
    for search_node in range(len(matrix[current_node])):

        if matrix[current_node][search_node] and search_node not in visit:
            visit = dfs(search_node, matrix, visit)
    return visit

def bfs(start_node):
    global matrix
    queue = [start_node]
    visit = [start_node]
    while queue:

        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in visit:
                queue += [search_node]
                visit += [search_node]
    return visit            

resultD = dfs(V, matrix, [])
resultB = bfs(V)
for i in range(len(resultD)):
    print(resultD[i], end=" ")
print()
for i in range(len(resultB)):
    print(resultB[i], end=" ")