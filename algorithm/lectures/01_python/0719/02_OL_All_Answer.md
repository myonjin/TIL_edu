# online_lab

실습 1-1. 산술연산자를 활용한 공식 만들기

```python
lower_x = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
upper_x = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
print(round(lower_x,4),round(upper_x,4))
```

실습 2-2. 문자열 메소드 이해 및 문제 해결

```python
s = input()

result = ''
for char in s:
    if char.isalpha() or char == ' ':
        result += char


print(result.title())
```

실습 2-3. 문자열 슬라이싱에 대한 이해

```python
str_lst = input('문자열을 입력하세요. : ').lower().split(' ')
condition = (str_lst[0][-1] == str_lst[1][0]) and (str_lst[1][-1] == str_lst[-1][0]) 
if condition:
    print('Pass')
else:
    print('Fail')
```

실습 2-4. 산술연산자를 활용한 공식 만들기

```python
steak = 50000
VAT = int(steak*0.15)
print(f'스테이크{steak:>9,}\n+ VAT{VAT:>10,}\n총계 ₩{(steak+VAT):>10,}')
```

실습 2-5. 딕셔너리와 리스트 특징 이해 및 메소드 활용 예제

```python
# 딕셔너리를 사용한방법
grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]
grain_dict = dict(grain_lst) # key는 작물명, values는 작물 가격이 들어있는 딕셔너리가 생성된다
grain_label = list(grain_dict.keys()) # 각각의 key, value들을 따로 받는다.
grain_price = list(grain_dict.values())
print(grain_label[grain_price.index(max(grain_price))]) #가장 높은 가격이 있는 index를 찾아 인덱싱한다.
```