from collections import deque
n = 19
edges = [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [4, 11], [5, 12], [5, 13], [6, 14], [6, 15], [6, 16], [8, 17], [8, 18]]

def sol(n, edges):
    dq = deque([])

    dq.append(edges[0])

    while dq:
        rootEdge = dq.popleft()

        for i in edges:
            if i[0] == rootEdge[]