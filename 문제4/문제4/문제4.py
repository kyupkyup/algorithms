INF = 987654321
new_cost = 987654321
adj[20000, 20000]

def solution(src, V, skip):
    dist = [V, INF]
    dist[src] = 0

    


def dijkstra(n, s, a, b, fares):
    result = []
    for i in range(len(fares)):
        adj[fares[0]].append([fares[1], fares[2]])
        adj[fares[1]].append([fares[0], fares[2]])
    result = dijkstra(s, n+1, -1 )

    new_cost = min(new_cost, result[a] + result[b])