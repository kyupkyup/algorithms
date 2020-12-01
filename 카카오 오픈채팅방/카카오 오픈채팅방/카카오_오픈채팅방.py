
record =["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
def solution(record):
    memory = dict() # 사전을 활용한 풀이 
    temp = []
    answer = []
    current_people = []
    stack = []
    for i in range(len(record)): 
        temp.append(record[i].split(" ")) # 엔터를 기준으로 모든 record를 분리해서 temp에 담아줌
    #TEMP = ["enter", "아이디", "닉네임"]
    for i in range(len(temp)):
        # 나갔을때 기록이 남아있어야함
        if temp[i][0] == "Enter":  # 엔터일 경우 메모리에 아이디를 key값, 닉네임을 벨류 값으로 넣어줌
            memory.update({temp[i][1] : temp[i][2]})
            current_people.append([temp[i][1], temp[i][0]]) # 현재 있는 사람을 기록해둠
        elif temp[i][0] == "Leave":
            current_people.append([temp[i][1], temp[i][0]]) # 나간다면 현재 있는 사람에서 삭제 
                                                            # memory에는 해당 기록을 남겨둠 -> 
                                                            # change했을 때 메모리에 있는 사람이 다 바뀌어야하기때문에
        elif temp[i][0] == "Change":
            memory[temp[i][1]] = temp[i][2]
            
    for i in range(len(current_people)):
        if current_people[i][1] =="Enter":
            answer.append(memory[current_people[i][0]]+"님이 들어왔습니다.") # 메모리 기준으로 엔터인 사람들은 마지막 닉네임으로 입력
        elif current_people[i][1] == "Leave":
            answer.append(memory[current_people[i][0]]+"님이 나갔습니다.") # 메모리 기준으로 나간 사람들 또한 마지막 닉네임으로 출력

    return answer           

print(solution(record))