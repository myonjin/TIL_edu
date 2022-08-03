# Problem A.

```python
def movie_info(movie):
    pass 
    # 여기에 코드를 작성합니다.    
    # print(movie)
    #new dict
    result={'id' : movie.get('id'),
    'title' : movie.get('title'),
    'poster_path' : movie.get('poster_path'),
    'vote_average' : movie.get('vote_average'),
    'overview' : movie.get('overview'),
    'genre_ids' : movie.get('genre_ids')}
    return result
```

movie.get(' ') : ' '안이 키값이고 get을 쓰면 value 값을 구한다 

항상 return 넣는거 있지 말기. 

for 문 안해도 하나하나 쓰는걸로 해도 된다 



# Problem B.

```python
name=[] 
    for i in movie.get('genre_ids'): # [18,80]
        for j in genres:
            if j["id"] == i:
                name.append(j['name'])
```

[18,80]인 값에 있는 리스트의 'name'의 value 값을 찾아야한다

먼저 genre_ids  가 18,80인 리스트를 찾기위해 for문으로 순회해서 전체값에서 찾아본다

그 장르 안에있는 j중에 id값이 i 랑 같으면 그 j리스트에 있는 name을 추가 해준다



- 어떤값을 순회해서 찾는거니깐 항상 for문으로 생각해보기 
- 굳이 range(len())을 쓸필욘없다



# Problem C.

```python
def movie_info(movies, genres):
    pass
    movlist=[]
    # 여기에 코드를 작성합니다.  
    for k in range(len(movies)):
        name=[] 
        for i in movies[k].get('genre_ids'): 
            for j in genres:
                if j["id"] == i:
                    name.append(j['name'])

                

        result={'id' : movies[k].get('id'),
        'title' : movies[k].get('title'),
        'poster_path' : movies[k].get('poster_path'),
        'vote_average' : movies[k].get('vote_average'),
        'overview' : movies[k].get('overview'),
        'genre_names' : name}
        movlist += [result]    
    return movlist
```



맨처음 B에 했던 문제를 계속 반복시키는거니깐 for문으로 하면된다고 생각했다.

하나씩 i 인값을 0부터 대입해보니 영화목록들이 떳다

그래서 for i in 을 써서 0부터 전체 길이 까지 넣어 주었따

마지막에 movlist=[]라는 리스트를 만들어주어서 for 문으로 반복한것을 추가해준다.

# Problem D.

```python

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
```



```python
movies_json = open(f'data/movies/{A}.json', encoding='utf-8')
movies_list = json.load(movies_json)
```

해석: data안 movies안 {A}이름의 .json 파일을 연다 movies_list는 그것을 로드한 목록

A= id 값의 리스트값들을 순회해서 만들어준다

open ( A )값 리스트 들을 열어주고 

그 "revenue"값을 찾아준다 

그런다음 조건문을 만들어주고 

해당하는 [i] 인덱스의 title을 찾는다

# Problem E.

```python
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
    
```

앞의문제와 비슷하게 

```python
if  "12"==movies_list["release_date"][5:7]:
    
```

- release_date 의 값이 12와 비슷한걸 찾아야하는데 12는 문자열이므로 "12" << 를 붙여준다