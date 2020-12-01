

s="ababcdcdababcdcd"

def solution(s):
    answer= len(s)
    # 몇 번 잘라야 하는지 n//2 만큼 실행 -=> n//2 이상이 되면 무조건 자를 수 없는 경우기 때문에
    for step in range(1, len(s)//2 + 1): #for 문의 마지막까지 실행해야 하기에 +1 을 해줌
        compressed = "" # 압축할 문자열
        count = 1
        for cut in range(0, len(s), step): # 각 커팅되는 문자열
            # 이전 문자열과 다음 문자열이 같다면 카운트를 플러스 하면서 다음 커트로 넘겨줌
            prev = s[cut:cut+step]
            next_word = s[cut+step:step+cut+step] # 다음 문자열
            
            if prev == next_word:
                count += 1
                prev = next_word
            else:
                
                if count < 2:
                    compressed += prev
                else:
                    compressed += str(count) + prev
                count = 1

        answer = min(answer,len(compressed))
    return answer

print(solution(s))
