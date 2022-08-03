import requests
from pprint import pprint


def popular_count():
    
   
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=6aff6c96fa8121c83d1a49c01d1407b3&language=ko-KR&page=1'

    response = requests.get(URL).json()
    
    results = response.get('results')
    
    return len(results)
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
