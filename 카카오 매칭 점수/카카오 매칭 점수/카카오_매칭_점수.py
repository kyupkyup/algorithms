word = "Muzi"
pages =["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]

def solution(word, pages):
    point = 0
    answer_arr = []
    basic_poin = []
    
    for i in range(len(pages)):
        basic_poin.append(basic_point(pages[i], word.lower())) 

    link_point = link_check(pages, basic_poin)
    
    for i in range(len(pages)):
        answer_arr.append(basic_poin[i] + link_point[i])
    return answer_arr.index(max(answer_arr))


def basic_point(pages, word):
    count = 0
    global alphabet
    temp = ""
    for i in range(len(pages)):
        if pages[i] in alphabet:
            temp += pages[i]
        else:
            temp+=" "
        words_arr = temp.split(" ")
    for each_word in words_arr:
        if word == each_word.lower():
            count += 1
    return count


def link_check(pages, basic_point):
    # 배열의 각 인덱스마다 본인에게 연결된 페이지 기록
    answer = []
    link = []
    my_link=[]
    my_link_point = [0 for i in range(len(pages))]
    out_link = []
    out_link_point = [0 for i in range(len(pages))]
    for i in range(len(pages)):
        words_arr= pages[i].split("/>")
        for word in words_arr:
            if "content=" in word:
                my_link.append(word[word.find("content=")+8:])
    print(my_link)


    for page in range(len(pages)):
        # 외부링크 수 구하고
        # 만약 그 외부링크가 마이 링크 중 있으면 마이 링크 점수 플러스
        words_arr = pages[page].split(">")
        temp = []
        for word in words_arr:
            if "a href" in word:
                temp.append(word[word.find("a href=")+7:])
        out_link.append(temp)

    for i in range(len(out_link)):
        out_link_point[i] += len(out_link[i])
    print("외부 링크" + str(out_link_point))

    for j in range(len(out_link)):
        for m in range(len(out_link)):
            if j != m:
                for k in range(len(out_link[m])):
                    if my_link[j] == out_link[m][k]:
                        # 외부에서 나에게 오는 점수가 외부 점수 / 외부로 연결된 수
                        my_link_point[j] += basic_point[m] / len(out_link[m])
    print("외부에서 오는" + str(my_link_point))

    print("결과" + str(answer))
    return my_link_point


print(solution(word, pages))