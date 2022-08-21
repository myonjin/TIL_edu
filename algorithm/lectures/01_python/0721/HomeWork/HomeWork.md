# HomeWork

## 위치 인자와 키워드 인자
- 4번 : 키워드 인자 뒤에 위치 인자가 올 수 없다.
```python
def ssafy(name, location='서울’):
    print(f'{name}의 지역은 {location}입니다.')
# (1)
ssafy('가흔')
# (2)
ssafy(location='부울경', name='승현')
# (3)
ssafy('지우', location='서울')
# (4)
ssafy(name='승호', '광주')
```

## 가변 인자 리스트
```python
def my_avg(*args):
    return sum(args) / len(args)

def my_avg(*args):
    # 전체 합
    total = 0
    # 전체 길이
    length = 0

    # 전체 순회
    for num in args:
        total += num
        length += 1
    # 평균
    return  total / length


my_avg(77, 83, 95, 80, 70) # => 81.0
```

## 반환값
```python
def my_func(a, b):
    c = a + b
    print(c)
result = my_func(3, 7)
```
- my_func 함수는 return 값이 없기 때문에 result 변수에는 `None`이 할당된다. 왜냐하면 파이썬은 return 값을 정의하지 않은 함수는 자동으로 None을 반환하도록 되어 있기 때문이다.

## 이름 공간(Namespace)
LEGB
1. Local Scope
2. Enclosed Scope
3. Global Scope
4. Built-in Scope

## 매개변수와 인자, 그리고 반환
- 답: 1번, python은 함수 반환값이 여러개의 객체이면, 그 객체들을 튜플로 묶어서 반환한다.

(1) 함수는 오직 하나의 객체만 반환할 수 있으므로
'return a, b＇와 같이 쓸 수 없다.
(2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 매개변수(parameter)는 함수를 선언할 때 설정한 값이며,
전달 인자(argument)는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 함수 선언 시 매개변수 앞에 * 을 붙이고,
이 때는 함수내에서 tuple로 처리 된다.

## 재귀 함수
- 코드가 직관적이고 간결하게 작성할 수 있다.
- 논리적으로 코드의 작동 순서를 파악하기 쉽다.
- 과도한 반복 호출로 인하여 메모리의 사용량이 늘어날 수 있다.
- 반복문에 비해서 상대적으로 계산을 마칠때까지 드는 시간이 길다.
    - 파이썬에서는 이걸 방지하기 위해서 1000번의 호출 제한을 두고 있습니다.
