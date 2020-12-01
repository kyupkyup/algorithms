import sys
sys.setrecursionlimit(10000)
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
answer_tra= []
answer_post = []
def solution(nodeinfo):
    global answer_tra, answer_post

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    x_only, y_only = [], []
    for i in range(len(nodeinfo)):
        x_only.append(nodeinfo[i][0])
        y_only.append(nodeinfo[i][1])
    x = sorted(nodeinfo, key=lambda x: x[0])
    y = sorted(nodeinfo, key=lambda x: x[1])

    traversal(y)
    post(y)
    answer=[]
    ans = []

    for i in answer_tra:
        answer.append(i[2])
    ans.append(answer)
    answer= []
    for i in answer_post:
        answer.append(i[2])
    ans.append(answer)
    return ans



def traversal(y): #전위순회 재귀함수
    global answer_tra
    # y리스트를 for문 돌려서 x값이 루트보다 작고, y값 또한 루트 보다 작은 리스트를 새로만든다. 
    # (왼쪽 순회) 
    #  없다면 오른쪽 순회 -> 현재 노드 보다 y값이 작고 x값이 큰 것이 있는지 확인
    #  둘 다 없으면 루트를 넣고 리턴 
    #
    # 루트의 y값을 제거하고 나머지 y값 리스트에서 최대값을 구해서 
    # 그 y값에 해당하는 x값이 존재하는지, 왼쪾 오른쪽
    if not y:
        return 

    new_left_y = []
    new_right_y = []
    for new_node in range(len(y)):
        if y[new_node][0] < y[-1][0] and y[new_node][1] < y[-1][1]: 
            new_left_y.append(y[new_node]) # x 값을 기준으로 새로운 왼쪽 서브트리를 
        elif y[new_node][0] >y[-1][0] and y[new_node][1] <y[-1][1]:
            new_right_y.append(y[new_node]) # x값을 기준으로 새로운 오른쪽 서브트리를 
    #루트 노드 찾아야함
    answer_tra.append(y[-1])
    traversal(new_left_y)
    traversal(new_right_y)
    
    return
def post(y): #후위순회 재귀함수
    global answer_post
    # y리스트를 for문 돌려서 x값이 루트보다 작고, y값 또한 루트 보다 작은 리스트를 새로만든다. 
    # (왼쪽 순회) 
    #  없다면 오른쪽 순회 -> 현재 노드 보다 y값이 작고 x값이 큰 것이 있는지 확인
    #  둘 다 없으면 루트를 넣고 리턴 
    #
    # 루트의 y값을 제거하고 나머지 y값 리스트에서 최대값을 구해서 
    # 그 y값에 해당하는 x값이 존재하는지, 왼쪾 오른쪽
    if not y:
        return 

    new_left_y = []
    new_right_y = []
    for new_node in range(len(y)):
        if y[new_node][0] < y[-1][0] and y[new_node][1] < y[-1][1]:
            new_left_y.append(y[new_node])
        elif y[new_node][0] >y[-1][0] and y[new_node][1] <y[-1][1]:
            new_right_y.append(y[new_node])
    #루트 노드 찾아야함
    post(new_left_y)
    post(new_right_y)
    answer_post.append(y[-1])

    return


print(solution(nodeinfo))