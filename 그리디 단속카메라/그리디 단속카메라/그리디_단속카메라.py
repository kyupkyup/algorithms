import copy
routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]

def solution(routes):
    routes = sorted(routes)
    answer = 0
    last_camera = 30000

    for route in reversed(routes):
        if last_camera > route[1]:
            answer += 1
            last_camera = route[0]
    return answer
print(solution(routes))