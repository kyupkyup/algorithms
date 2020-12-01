bridge_length = 100	
weight = 100	
truck_weights = [10]

def solution(bridge_length, weight, truck_weights):
    truck = 0
    stack_start = truck_weights
    stack_ing = []
    stack_end = []
    truck_time = []
    time = 0
    while True:
        if stack_end == stack_start: 
            return time
            break
        if len(truck_time) > 0:
            if max(truck_time) >= bridge_length:
                stack_end.append(stack_ing[0])
                del truck_time[0]
                del stack_ing[0]

        if truck < len(truck_weights): 

            if truck_weights[truck] + sum(stack_ing) <= weight: # 다리 진입
                truck_time.append(0)
                stack_ing.append(truck_weights[truck])
                truck += 1 

        time += 1
        for i in range(len(truck_time)):
            truck_time[i] += 1




print(solution(bridge_length, weight, truck_weights))
