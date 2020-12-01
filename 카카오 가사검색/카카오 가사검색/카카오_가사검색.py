
# 34.4 
# 효율성 0.8%
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    result = []
    for query in queries: # 쿼리 모두 순회
        if query[-1] == "?":
            temp = True # 접미사 - true
        elif query[0] == "?":
            temp = False #접두사 - false

        if query[-1] == "?" and query[0] == "?":
            temp = "al"
        count = 0
        for word in words: #word 모두 순회
            if temp == "al":  # "?????"
                if(len(word)) == len(query):
                    count+=1
                # 물음표의 개수만큼 전체에서 같은 위치 같은 문자의 수를 빼주면 됨
            elif temp == True: #접미사
                if query[:query.index("?")] == word[:len(word) - query.count("?")]: 
                    count +=1
            elif temp == False: # 접두사
                if query[query.count("?"):] == word[query.count("?"):]:
                    count += 1
        result.append(count)   
    return result
print(solution(words, queries))