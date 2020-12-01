from collections import deque
import copy
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
cnt = 0
 
def search(current_word, compare_word): # 한글자만 차이나는 워드를 검증하는 함수
    local_cnt = 0
    for i in range(len(current_word)):
        if compare_word[i] in current_word:
            compare_word.replace(compare_word[i],".")
            local_cnt += 1
    if local_cnt == len(current_word) - 1:
        return True
    else:
        return False

def bfs(dq, words, begin, target): #bfs 
    global cnt
    copy_words = copy.deepcopy(words)
    next_queue = deque([]) # 다음 단계의 queue
    if target not in words:
        cnt = 0
        return

    if not dq and not words:  # queue도 비고 워드도 비었는데 단어를  못 찾으면 0 리턴
        cnt = 0
        return

    while dq:
        current_word = dq.popleft() # 
        if current_word == target:
            return

        # 한 글자만 차이나는 word begin으로 변환 큐에 저장
        for compare_word in words[:]:  # word 를 순회하면서 단어를 비교
            if len([i for i in range(0,len(compare_word)) if compare_word[i]!=current_word[i]]) == 1:
                next_queue.append(compare_word)  #다음 큐에 삽입 
                words.remove(compare_word) # 워드에서 삭제해서 중복 검사 안하도록
    cnt += 1
    bfs(next_queue, words, begin, target)

def solution(begin, target, words):
    dq = deque([])
    dq.append(begin)

    bfs(dq, words, begin, target)
    return cnt


    
print(solution(begin, target, words))