N, M = map(int, input().split(" "))

profit = [list(map(int, input().split(""))) for i in range(N)]

profitList = [N][M] 



def calculate():
    # 1만 투자했을 때 기업에서 최대값 구하는 함수
    val = 0

    for k in range(N):
        val = max(profit[k][0], profit[k][1], profit[k][2])