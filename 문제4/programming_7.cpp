#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>
#include <cstdio>

#define MAX_V 20001

using namespace std;
const int INF = 9876541;
// 그래프의 인접 리스트. (연결된 정점 번호, 간선 가중치) 쌍을 담아야 한다.
vector< pair<int, int>> adj[MAX_V]; // 정점의 최대 개수 :: MAX_V
int n, s, a, b;

int now_cost = 987654321;

vector<int> dijkstra(int src, int V,int skip)
{
    // V만큼 배열을 INT_MAX로 초기화
    vector<int> dist(V, INF);
    dist[src] = 0; // 시작점은 0으로 초기화 한다. 

    priority_queue<pair<int, int> > pq;

    pq.push(make_pair(0, src)); // 시작점을 처음으로 우선순위 큐에 삽입

    while (!pq.empty())
    {
        // 우선순위 큐에 음의 가중치로 들어가 있으니 양으로 바꾸어준다.
        int cost = -pq.top().first;
        int here = pq.top().second;

        pq.pop();

        // 만약 지금 꺼낸 것보다 더 짧은 경로를 알고 있다면 지금 꺼낸것을 무시한다.
        if (dist[here] < cost)
            continue;

        // 인접한 정점들을 모두 검사.
        for (int i = 0; i < adj[here].size(); i++)
        {
            int there = adj[here][i].first;
            int nextDist = cost + adj[here][i].second;
            
            if (there == skip)
                continue;

            // 더 짧은 경로를 발견하면, dist[]를 갱신하고 우선순위 큐에 넣는다.
            // dist 벡터에는 시작점 -> there 위치까지의 최단 거리가 담겨있다.
            if (dist[there] > nextDist)
            {
                dist[there] = nextDist;
                pq.push(make_pair(-nextDist, there));
                
            }
        }
    }

    return dist;
}

int main()
{
    int k;
    cin >> k;
    cin >> n >> s >> a >> b;
    // n 은 노드 개수
    // s 는 출발지
    // a 는 a의 도착지점
    // b 는 b의 도착지점

    for (int i = 0; i < k; i++)
    {
        int x, y, z;
        // x -> y 비용 z
        cin >> x >> y >> z;
        adj[x].push_back({ y,z });
        adj[y].push_back({ x,z });
    }
    vector<int>result = dijkstra(s,n+1,-1); // 스타트에서 각 노드로 가는 경로 최소값

    now_cost = min(now_cost, result[a] + result[b]); // s -> a로 가는 값 + s-> b로 가는 최소값
    vector< pair<int, int>> temp;

    for (int i = 1; i <= n; i++)
    {
        if (i == s)
            continue;

        vector<int> this_result = dijkstra(i,n+1,s); // 1부터 증가하는 각각의 정점에서 각각의 노드로 가는 값
        
        now_cost = min(now_cost, result[i] + this_result[a] + this_result[b]); // s -> i로 가는 값 i -> a로 가는 값 -> i 에서 b로 가는 값

    }

    cout << now_cost;

    
    return 0;
}