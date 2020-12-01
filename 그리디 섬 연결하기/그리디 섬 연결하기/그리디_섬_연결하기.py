#
#  그리디와 그래프 접목
#  핵심은 가장 최선의 방법이 뭔지 찾아내는 것.
# 이 문제에서는 cost로 정렬해서 cost 별로 visited 를 만들어 cost의 최소값을 구해야함
#
#
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    costs.sort(key=lambda x:x[2])  # weight(비용) 기준으로 정렬
    result = 0
    visited = []

    frm, to, weight = costs[0]  # 가장 cost가 작은 기본 값
    visited = set()    # 중복없게 만들어주는 리스트
    result += weight   # 초기값
    visited.update([frm, to])   # 지금 visited 는 {0, 1} 

    while len(visited) < n:  # visited가 n 길이가 될때까지
        for cost in costs:   # costs 리스트 순회
            f, t, w = cost    # cost의 값들을 변수에 넣어줌
            if f in visited or t in visited:   #만약 출발점이나 도착점 중 하나가 visited에 있으면 
                if f in visited and t in visited:  # 그 중에서도 둘 다 있으면 이미 다리를 놓은 node이므로 제외
                    continue
                else:   # 출발점이나 도착점 중 하나가 있으면 그 곳에서부터 연결하면 됨
                    result += w   # weight를 결과에 더해주고( weight를 기준으로 정렬했으므로 무조건 최소값이란걸 기대할 수 있음)
                    visited.update([f,t])  # visited에 해당 노드 추가
                    break  # 다시 cost를 처음부터 순회하기 위해 브레이크 

    return result
print(solution(n, costs))