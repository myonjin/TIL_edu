### 08_python_online_lab



**데일리 실습 8-2 답안 및 해설**

```python
from datetime import date


class Person:
    # 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, date.today().year - year)

    def check_age(self):
        return self.age > 19

```

- `details`
  - classmethod로 이름과 연도를 넣으면, 나이를 구할 수 있다.
  - `date.today()`메소드를 사용하여 오늘 날짜를 가져오고, `date.today()`의 `year`를 통해 해당 날짜의 연도를 확인 가능하다.
- `check_age`

  - 인스턴스 메서드로 현재 인스턴스가 미성년자인지 확인할 수 있다.
