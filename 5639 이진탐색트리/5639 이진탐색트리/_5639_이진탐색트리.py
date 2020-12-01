
class Node:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

class binarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            current = self.root
            while True:
                if current.key > key:
                    if current.lchild == None:

                        current.lchild = Node(key)
                        break
                    current = current.lchild
                if current.key < key:
                    if current.rchild == None:
                        current.rchild = Node(key)
                        break
                    current = current.rchild
    def postOrder(self, node):
        s= []
        while True:
            while node: # 노드가 살아있는 동안 
                if node.rchild: # 오른쪽 노드가 존재한다면 
                    s.append(node.rchild) # s에 오른쪽 노드 푸쉬
                s.append(node) #현재 노드 푸쉬
                node = node.lchild # 노드 포인터를 를 왼쪽 노드로 이동 
            node = s.pop() # s에서 pop한 노드를 노드에 삽입 == 왼쪽 노드가 없을 경우 s에서 팝한 노드를 현재 노드로
            if node.rchild and (s[-1] if len(s) else None) == node.rchild: # 오른쪽 노드가 존재하거나 s 마지막 노드가 
                s.pop() 
                s.append(node)
                node = node.rchild
            else:
                print(node.key)
                node= None
            if not s:
                break

bst = binarySearchTree()
while True:
    try:
        key = int(input())
        bst.insert(key)
    except:
        break
print(bst)
bst.postOrder(bst.root)