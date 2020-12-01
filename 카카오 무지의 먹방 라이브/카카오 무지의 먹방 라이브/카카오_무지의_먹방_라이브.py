
food_times =[1,2]
k = 2

def solution(food_times, k):
    food_times.insert(0, 0)
    length = len(food_times)
    
    count = 0 # count는 내가 몇 초 동안 음식을 먹고있었는지
    # 푸드를 순회하면서 중지되는 시점에 먹고있던 포인터를 리턴하면됨
    pointer = 1 # 내가 현재 먹고 있는 음식을 포인팅
    while True:

        if count == k: # 방송이 정지되는 시점이 오면
            while food_times[pointer] == 0: # 내가 방송이 정지되는 시점에 먹을 음식이 0이면 다음 음식으로 넘어가야함
                pointer += 1               
                if pointer == length:  # 만약 그 0인 음식이 마지막이라면 맨 처음으로 넘어가야함
                    pointer = 1
            return pointer

        if food_times[pointer] != 0:  # 지금 먹을 음식이 0이 아니라면 그대로 1을 빼줌
            food_times[pointer] -= 1
            if sum(food_times) == 0:  # 모든 음식을 다 먹었으면 먹을게 없으니 -1 리턴
                return -1
        else:
            pointer += 1  # 먹을 음식이 0이라면 다음 음식으로 넘어감
            if pointer == length:
                pointer = 1  
            continue


        pointer += 1 # 다음 음식이 뭔지 알아야되므로 마지막에 한번 더 플러스 해줘서 다음 음식을 알아냄
        if pointer == length:
            pointer = 1            
        count += 1


print(solution(food_times,k))