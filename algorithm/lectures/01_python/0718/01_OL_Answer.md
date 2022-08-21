# online_lab

```python
score = {'python': 80, 'django': 89, 'web': 83}

# 1
score['algorithm'] = 90

# 2
score.update({'python': 85})

# 3
sum(score.values()) / len(score.values())
```

1. `dict[key] = value` 형식의 항목추가를 통해 algorithm 과목의 성적을 할당한다.
2. `dict.update()` 메소드를 통해, `python` 이라는 key를 가진 value를 85로 업데이트한다.
3. `sum`을 이용하여, score 딕셔너리의 값들의 합을 `len` 함수를 통해 구한 딕셔너리의 크기를 대상으로 나누어 전체 점수의 평균을 구한다.