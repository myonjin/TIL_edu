import json


def max_revenue(movies):
    pass 
    # 여기에 코드를 작성합니다.
    # Id 값을 찾는다 
    Num=0
    for i in range(len(movies)):
        A=movies[i]["id"]
         
        movies_json = open(f'data/movies/{A}.json', encoding='utf-8')
        movies_list = json.load(movies_json)
        if Num < movies_list["revenue"]:
            Num = movies_list["revenue"]
            name=movies[i]["title"]
            
    
        
    return name
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
