from collections import deque
import copy
# 그래프와 bfs

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
def solution(n, vertex):

    answer = 0
    visited = [-1] * (n + 1)  # 내가 방문한 노드 - -1 로 초기화
    adj = [[] for _ in range(n + 1)] # x -> y 
    for e in vertex: 
        x = e[0] # ex) 3과 연결된 노드를 찾아 배열에 append해줌  -  3,6 3,2 
        y = e[1] 
        adj[x].append(y)
        adj[y].append(x)
    
    bfs(1, visited, adj)

    max_ = max(visited)
    for i in visited:
        if i == max_:
            answer += 1
    return answer

def bfs(node, visited, adj):
    count = 0
    dq = deque([[node, count]])  # 카운트를 각 노드에 넣어줌

    while dq:   # dq 
        value = dq.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                dq.append([e, count])
        
    return
    

print(solution(n,vertex))