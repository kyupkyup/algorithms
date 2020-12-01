
n = 12
weak = 	[1, 5, 6, 10]
dist =	[1, 2, 3, 4]	

def solution(n, weak, dist):
    visit = [False for i in range(len(weak))]
    answer = []
    # 오른쪾으로 점검
    # weak_point에서 dist를 더한 후
    # 그것보다 작은 weak 포인트 visit -n 을 하고도 작은 weak_point visit 처리
    for weak_point in range(len(weak)):
        count = 1

        for dist_length in range(len(dist)-1,0,-1):
            if not False in visit:
                # 모든 위크포인트를 다 순회했으면
                answer.append(count)
            else:
                visit[weak_point] = True
                for temp in range(weak_point, len(weak)):
                    visit[temp] = True
                    if visit[temp] == True:
                        continue
                    if weak[temp] <= weak[weak_point] + dist[dist_length] and visit[temp] == False:
                        visit[temp] = True
                    elif weak[weak_point] + dist[dist_length] >= 12:
                        if weak[temp] <= weak[weak_point] + dist[dist_length] - 12 and visit[temp] == False:
                            visit[temp] = True
                    count += 1
    return min(answer)
    # 왼쪾으로르 점검
    # weak_ point보다 작은 경우 visit 0 보다 작을 경우 12를 더해서 그 값보다 큰 weak_point visit 처리

print(solution(n, weak, dist))