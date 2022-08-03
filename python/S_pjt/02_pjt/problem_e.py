import requests
from pprint import pprint


def credits(title):
    people=[]
    gam=[]
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=6aff6c96fa8121c83d1a49c01d1407b3&language=ko-KR&query={title}&page=1&include_adult=false'
    response = requests.get(URL).json()
    results = response.get('results')
    if results==[]:
        return None
    ids=results[0].get('id')

    URL = f'https://api.themoviedb.org/3/movie/{ids}/credits?api_key=6aff6c96fa8121c83d1a49c01d1407b3&language=ko-KR'
    response_2 = requests.get(URL).json()
    a=response_2.get('cast')
    for i in  range(len(a)):    
         if a[i].get('cast_id')<10:
            people.append(a[i].get('name'))

    b=response_2.get('crew')
    for i in  range(len(b)):    
         if b[i].get('department')=='Directing':
            gam.append(b[i].get('name'))

    # a=recommend[0].get('results')
    # final=[]
    # for i in a:
    #     i.get('title')
    #     final.append(i.get('title'))
    return {'case':people,'directing':gam}
    
    
# 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
