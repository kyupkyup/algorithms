
n = 6
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5, 6]]

def solution(n, results):

    arr = []
    for i in range(1, n+1):
        arr.append([i, 0 ,0 ])

    for a in arr:
        for vertex in results:
            if a[0] == vertex[0]:
                a[1] += 1
            if a[0] == vertex[1]:
                a[2] += 1
        print(arr)
solution(n, results)