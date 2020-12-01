import queue
N, T = map(int, input().split(" "))
arr = [list(map(int, input().split(" "))) for i in range(N)]

def BFS(sortedArr):
    global T
    count = 0
    visit= list()
    q = queue.Queue()
    q.put([0,0])


    while q:

        node = q.get(0)
        if node[1] == T:
            return count

        if node not in visit:
            visit.append(node)
            while :
                q.put(sortedArr[i])
                i += 1


               # 범위 안에있는 노드 찾아서 queue에 넣어줘야되는데 범위 안에 있는 노드를 어케 ㅏㅊㅈ아암ㅇ럄젇램젇ㄻ잳럼ㄹ므잗르민우루맫ㄻㅈㄷ럼ㅈ대럼ㅈㄷ랴ㅐㅁ덜
               # for 문 돌리자니 어뗴ㅒ랒메덜
            count += 1
    return 

def Search():
    global arr
    sortedArr= sorted(arr, key=lambda ar : ar[1])
    return sortedArr
sortedArr = Search()
BFS(sortedArr)