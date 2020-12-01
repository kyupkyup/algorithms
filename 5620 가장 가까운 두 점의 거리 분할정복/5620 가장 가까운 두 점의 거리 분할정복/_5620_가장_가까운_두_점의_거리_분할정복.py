
import copy
N = int(input())

arr = [list(map(int, input().split(" "))) for i in range(N)]
copy = copy.deepcopy(arr)
