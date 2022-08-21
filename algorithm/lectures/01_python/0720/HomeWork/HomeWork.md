조건 표현식

# # HomeWork

## Built-in Function

```python
sum(). len(), print(), max(). min(), avg()
```



## 홀수만 담기

```python
a = list(range(1, 51, 2))
print(a[::2])
```



## 반복문으로 네모 출력

```python
n = 5
m = 9

for height in range(m):
    for width in range(n):
        print('*', end='')
    print()
```



## 조건 표현식

```python
temp = 36.5
if temp >= 37.5:        
    print('입실 불가')
else:
    print('입실 가능')
```

```python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```



## 정중앙 문자

```python
def get_middle_char(word):
    # 짝수 인지 아닌지 판별 하려면 우선 길이부터 알아야한다.
    word_len = len(word)
    middle_idx = word_len // 2
    # 2로 나눈 나머지에 따라서 홀수 짝수 구분
    if word_len % 2:
        # 홀수   
        middle = word[middle_idx]     
    else:
        # 짝  
        # 전체 길이가 6이라면
        # 6 // 2 -> 3
        # 내가 필요로 하는 인덱스 번호는
        # 2, 3
        # [0, 1, **2, 3**, 4, 5]
        # word[2:4]
        middle = word[middle_idx-1:middle_idx+1]
    return middle
    
```

```python
get_middle_char('ssafy’) # => a
get_middle_char('coding’) # => di
```


