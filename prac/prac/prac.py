genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    
    genres_play = {}
    play_list ={}
    maxPlayList = []
    realAns = []
    for i in range(len(genres)):
        genres_play[genres[i]] = genres_play.get(genres[i], 0) + plays[i] # 장르와 플레이수 짝
    
    for i in range(len(plays)):
        play_list[i] = play_list.get(i, 0) + plays[i] # 번호와 플레이수 짝
    
    maxPlay = max([(value, key) for key, value in play_list.items()])[1]
    del play_list[maxPlay]
    secondMaxPlay = max([(value, key) for key, value in play_list.items()])[1]


    maxGenres = max([value, key] for key, value in genres_play.items())[1]
    print(secondMaxPlay)
    while genres_play:
        answer=[]
        for i in range(len(genres)):
            if genres[i] == maxGenres:
                if i == maxPlay and answer:
                    answer.insert(0, i)
                elif i == secondMaxPlay:
                    answer.insert(i)
            
            else:
                i += 1
            realAns.append(answer)   
        
        del genres_play[maxGenres]


    print(realAns)

    return answer

def f1(x):
    return 
solution(genres, plays)