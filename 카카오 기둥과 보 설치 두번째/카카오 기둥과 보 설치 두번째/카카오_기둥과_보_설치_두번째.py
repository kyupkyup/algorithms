

n = 5
build_frame = 	[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
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
         
            elif [x, y, 1] in answer: # 왼쪽에서 오는 보
                return True
            elif [x+1, y, 1] in answer: # 오른쪽에서 오는 보
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
    if [x, y, build] in answer:
        # 이 내용을 삭제하기 위해 여기에 연결된 기둥이나 보가, 이 내용이 없어졌을때도 문제가없는지 확인 필요
           
        # 보의 경우 - 왼쪽 오른쪽 보가 기둥에 연결되어있으면 ㄱㅊ
        # 보의 경우 - 왼쪾 오른쪽 기둥에 보가 연결되어 있으면 ㄱㅊ

        # 기둥의 경우 - 왼쪽 오른쪽 보가 기둥에 연결되어있으면 ㄱㅊ 
        # 기둥의 경우 - 기둥이 연결되면 안됨

        if build == 1:
            if [x + 1 , y, 1] in answer: # 오른쪽 보가 존재하면
                if not [x, y-1, 0] in answer and not [x+1, y-1, 0] in answer:# 오른쪽 보가 기둥에 연결되어있으면 
                    return answer
                        
            if  [x-1, y, 1] in answer: #왼쪽 보가 존재하면
                if not [x-1, y-1, 0] in answer and not [x, y-1, 0] in answer: # 왼쪽 보의 양쪽에 기둥이 존재하는지
                    return answer

            # 왼쪽 기둥이 존재하면
            if [x, y, 0] in answer:
                if not [x-1, y, 1] in answer:
                    return answer
            #오른쪽 기둥이 존재하면
            if [x+1, y, 0] in answer:
                if not [x+1, y, 1] in answer:
                    return answer
            answer.remove([x,y,build])
            return answer
        elif build == 0:
            #왼쪽 보가 존재하면
            if [x-1, y+1, 1] in answer:
                if not [x-1, y, 0] in answer and (not [x-2, y+1, 1] in answer and not [x,y,1] in answer): # 왼쪽 보에 기둥이 연결안되있거나 양쪽 보에 연결안되있으면
                    #기둥이 없고, (양쪽 보 중에 하나라도 연결이 안되있따면)
                    return answer
            #오른쪽 보가 존재하면
            if [x,y+1, 1] in answer:
                if not [x+1, y, 0] in answer and (not [x-1, y+1, 1] in answer and not [x+2, y+1, 1] in answer):
                    return answer
            
            #윗기둥이 존재하면 양 옆으로 보가 존재하는지
            if [x, y+1, 0] in answer:
                if not [x-1, y+1, 1] in answer or not [x,y+1,1] in answer:
                    return answer
            answer.remove([x,y,build])
            return answer
    # x,y 좌표의 기둥이나, 보가 있는지 확인해서
    # 해당 기둥, 보가 있다면 delete 아니면 그냥 리턴

def add(x, y, build, answer):
    # answer 에서 체크를 통해 가능한지 안한지 확인해서 가능하다면 
    # answer에 집어넣어줌
    if not answer:
        answer.append([x,y, build])
        return answer

    if build == 0:
        if check(x,y,build, answer):
            answer.append([x,y,0])
            return answer
        else:
            return answer
    elif build == 1:
        if check(x,y,build,answer):
            answer.append([x,y,1])
            return answer
        else:
            return answer
print(solution(n, build_frame))