import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.  
    # ID 값을 받으면 Name을 출력하게 

    name=[] 
    for i in movie.get('genre_ids'): # [18,80]
        for j in genres:
            if j["id"] == i:
                name.append(j['name'])

            


    result={'id' : movie.get('id'),
    'title' : movie.get('title'),
    'poster_path' : movie.get('poster_path'),
    'vote_average' : movie.get('vote_average'),
    'overview' : movie.get('overview'),
    'genre_names' : name}
    return result
    
    




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))


# 18: Drama 80: crime
