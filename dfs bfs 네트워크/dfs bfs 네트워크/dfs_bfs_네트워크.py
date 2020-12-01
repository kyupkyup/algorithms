
n  = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
#[[1, 1, 0,1,0], [1,1,1, 1, 1], [0,1, 1, 1,0], [1,0,1,1,1],[0,1,0,1,1]]


def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]   #visited [0,0,0]
    pointer = 0
    while 0 in visited:
        if visited[pointer] == 0:
            dfs(computers, visited, pointer)
            answer += 1
        pointer += 1
    return answer

def dfs(computers,visited, start):

    stack = [start] # dfs 
   
    while stack:
        current_computer = stack.pop()
        if visited[current_computer] == 0:
            visited[current_computer] = 1

        for connected_computer in range(n):
            if computers[current_computer][connected_computer] == 1 and visited[connected_computer] == 0:
                stack.append(connected_computer)
    return

        

print(solution(n, computers))