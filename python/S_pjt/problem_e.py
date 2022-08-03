import json
from optparse import TitledHelpFormatter


def dec_movies(movies):
    pass 
    # 여기에 코드를 작성합니다.
    title=[]
    for i in range(len(movies)):
         A=movies[i]["id"]       
         movies_json = open(f'data/movies/{A}.json', encoding='utf-8')
         movies_list = json.load(movies_json)
         if  "12"==movies_list["release_date"][5:7]:
            title.append(movies[i]["title"])
    return title
    
    
    
    
    # Num=0
    # for i in range(len(movies)):
    #     A=movies[i]["id"]
         
    #     movies_json = open(f'data/movies/{A}.json', encoding='utf-8')
    #     movies_list = json.load(movies_json)
    #     if Num < movies_list["revenue"]:
    #         Num = movies_list["revenue"]
    #         name=movies[i]["title"]   
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
