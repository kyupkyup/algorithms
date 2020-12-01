
class node():
    def __init__(self):
        self.parents = None
        self.child = []

node_num = int(input()) # 노드개수
info = list(map(int,input().split())) # 부모노드 
del_node_num = int(input()) # 지울 노드

tree = [0]*node_num # 노드 개수만큼 트리 리스트 생성
for i in range(node_num):
    if tree[i] == 0: # 트리 리스트가 비어있으면
        tree[i] = node() # node 생성 노드 생성
    tree[i].parents = info[i] # 그 트리에 부모 정보입력 

    if tree[info[i]] == 0: # 부모 노드 인덱스가 0이면
        tree[info[i]] = node() # 부모 노드에 노드 생성 -> 

    if info[i] == -1: # 루트를 만날때까지 반복
        root = i
    else:
        tree[info[i]].child.append(i) # 
    

leaf = 0

if tree[del_node_num].parents != -1: # root node가 아닌경우
    tree[tree[del_node_num].parents].child.remove(del_node_num) # del node link
else:
    tree[del_node_num].child = []
    leaf = -1
    
q = tree[root].child

while q:
    Next= []
    for v in q:
        if len(tree[v].child) == 0:
            leaf +=1
        for u in tree[v].child:
            Next.append(u)
    q = Next
if leaf == -1:
    print(leaf+1)
elif leaf == 0:
    print(1)
else:
    print(leaf)