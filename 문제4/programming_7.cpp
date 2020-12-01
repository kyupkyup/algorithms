#include <iostream>
#include <vector>
#include <queue>
#include <limits.h>
#include <cstdio>

#define MAX_V 20001

using namespace std;
const int INF = 9876541;
// �׷����� ���� ����Ʈ. (����� ���� ��ȣ, ���� ����ġ) ���� ��ƾ� �Ѵ�.
vector< pair<int, int>> adj[MAX_V]; // ������ �ִ� ���� :: MAX_V
int n, s, a, b;

int now_cost = 987654321;

vector<int> dijkstra(int src, int V,int skip)
{
    // V��ŭ �迭�� INT_MAX�� �ʱ�ȭ
    vector<int> dist(V, INF);
    dist[src] = 0; // �������� 0���� �ʱ�ȭ �Ѵ�. 

    priority_queue<pair<int, int> > pq;

    pq.push(make_pair(0, src)); // �������� ó������ �켱���� ť�� ����

    while (!pq.empty())
    {
        // �켱���� ť�� ���� ����ġ�� �� ������ ������ �ٲپ��ش�.
        int cost = -pq.top().first;
        int here = pq.top().second;

        pq.pop();

        // ���� ���� ���� �ͺ��� �� ª�� ��θ� �˰� �ִٸ� ���� �������� �����Ѵ�.
        if (dist[here] < cost)
            continue;

        // ������ �������� ��� �˻�.
        for (int i = 0; i < adj[here].size(); i++)
        {
            int there = adj[here][i].first;
            int nextDist = cost + adj[here][i].second;
            
            if (there == skip)
                continue;

            // �� ª�� ��θ� �߰��ϸ�, dist[]�� �����ϰ� �켱���� ť�� �ִ´�.
            // dist ���Ϳ��� ������ -> there ��ġ������ �ִ� �Ÿ��� ����ִ�.
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
    // n �� ��� ����
    // s �� �����
    // a �� a�� ��������
    // b �� b�� ��������

    for (int i = 0; i < k; i++)
    {
        int x, y, z;
        // x -> y ��� z
        cin >> x >> y >> z;
        adj[x].push_back({ y,z });
        adj[y].push_back({ x,z });
    }
    vector<int>result = dijkstra(s,n+1,-1); // ��ŸƮ���� �� ���� ���� ��� �ּҰ�

    now_cost = min(now_cost, result[a] + result[b]); // s -> a�� ���� �� + s-> b�� ���� �ּҰ�
    vector< pair<int, int>> temp;

    for (int i = 1; i <= n; i++)
    {
        if (i == s)
            continue;

        vector<int> this_result = dijkstra(i,n+1,s); // 1���� �����ϴ� ������ �������� ������ ���� ���� ��
        
        now_cost = min(now_cost, result[i] + this_result[a] + this_result[b]); // s -> i�� ���� �� i -> a�� ���� �� -> i ���� b�� ���� ��

    }

    cout << now_cost;

    
    return 0;
}