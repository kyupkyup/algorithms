
import copy
n = 5
build_frame = 	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
answer = []
def solution(n, build_frame):
    # for 문 순회로 모든 빌드 프레임을 돌아줌
    global answer
    for i in range(len(build_frame)):
        if build_frame[i][3] == 0:
            answer = delete(build_frame[i][0], build_frame[i][1], build_frame[i][2], answer)
        elif build_frame[i][3] == 1:
            answer = add(build_frame[i][0], build_frame[i][1], build_frame[i][2], answer)
    
    answer = sorted(answer, key=lambda x : (x[0], x[1], x[2]))
    return answer
    #answer 정렬 x, y, build 순서대로
    # 




def check(x, y, build, answer):
    # 보일 경우 그 좌표에 기둥이 연결되어있는지? 
    # 기둥일경우, 바닥인지, 보와 연결되어 있는지, 다른 기둥과 연결되어 있는지?
    # 두가지 케이스를 나눠서 
    if build == 0: #기둥
        if y == 0: # 바닥인 경우
            return True
        else:
                # answer 순회하면서 다른 기둥이나 보에 연결되어있는지
            if [x,y-1,0] in answer : # 기둥
                return True
         
            elif [x-1, y, 1] in answer: # 왼쪽에서 오는 보
                return True
            elif [x, y, 1] in answer: # 오른쪽에서 오는 보
                return True
        return False
    elif build == 1: #보 
        if [x, y-1, 0] in answer:  # 보가 왼쪽 기둥이 연결되어있는지
            return True
        elif [x+1,y-1,0] in answer:# 보가 오른쪽 기둥에 연결
            return True 
        elif [x-1, y, 1] in answer and [x+1, y, 1] in answer: # 보가 양쪽 보에 동시에 연결되는지
            return True
        return False


def delete(x, y, build, answer):
    temp = copy.deepcopy(answer)
    temp.remove([x,y,build])
    for i in temp:
        if not check(i[0], i[1], i[2], temp):
            return answer
    return temp



def add(x, y, build, answer):
    temp = copy.deepcopy(answer)
    temp.append([x,y,build])
    for i in temp:
        if not check(i[0], i[1],i[2], temp):
            return answer
    return temp


print(solution(n, build_frame))