# WorkSHop

## 간단한 N의 약수
```
입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오
[제약 사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
[입력]
입력으로 정수 N이 주어진다.
[출력]
정수 N의 모든 약수를 오름차순으로 출력한다.
[입력 예시]
10
[출력 예시]
1 2 5 10
```
```python
N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')
```

## List의 합 구하기
- 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.
```python
def list_sum(numbers):
    result = 0 
    for num in numbers:
        result += num
    return result

def list_sum(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]

list_sum([1, 2, 3, 4, 5]) # => 15
```

## Dictionary로 이루어진 List의 합 구하기
```python
def dict_list_sum(informations):
    result = 0
    for info in informations:
        # info - {'name': 'kim', 'age': 12}
        result += info['age']
    return result

dict_list_sum([{'name': 'kim', 'age': 12},
{'name': 'lee', 'age': 4}]) # => 16
```

## 2차원 List의 전체 합 구하기
- 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는 all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.
```python
def all_list_sum(num_list):
    result = 0
    for i in range(len(num_list)):
        for j in range(len(num_list[i])):
            result += num_list[i][j]
            # i 0
            # j 0 => 1
            # i 1
            # j 0 => num_list[1][0]
    return result
all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]) # => 55
```

## 숫자의 의미
```python
def get_secret_word(numbers):
    word = ''
    for number in numbers:
        # chr(65) >> 'A'
        word += chr(number)
    return word

get_secret_word([83, 115, 65, 102, 89]) # => ‘SsAfY’
```

##  내 이름은 몇일까?
```python
def get_secret_number(word):
    result = 0
    for char in word:
        result += ord(char)
    return result
get_secret_number('happy') # => 546
```

## 강한 이름
```python
```
