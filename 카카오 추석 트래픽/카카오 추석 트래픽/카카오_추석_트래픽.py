
import datetime
lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",   
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
def solution(lines):
    # lines의 맨처음과 맨마지막 값을 뺴고 맨처음의 소요시간을 뻄

    # 그 사이를 0.001 단위로 for문을 돌면서 각각의 문자열 사이에 있는 경우가 몇개인지 계산
    temp1, temp2, temp3 = "", "",""
    date_line=[]
    time_line =[]
    new_date_line = []
    seconds=[]
    for i in range(len(lines)):
        temp1, temp2, temp3 = lines[i].split(" ")
        date_line.append(temp1+" "+temp2)
        seconds.append(temp3[:-1])
    for line in date_line:
        new_date_line.append(datetime.datetime.strptime(line, "%Y-%m-%d %H:%M:%S.%f"))
    print(new_date_line[-1] - new_date_line[0] - datetime.datetime.strptime(seconds[0], "%S"))


        



print(solution(lines))