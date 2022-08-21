# class 정의를 위해 class ClassName
class Pokemon:
    # 푸키먼들이 공통적으로 가지는 속성들
    # 클래스 변수
    info = '푸키먼...'
    population = 0
    bell_population = 0

    # 새 포켓몬이 태어났을 때
    # 생성자
    # 인스턴스 메서드
    def __init__(self, name, lv=1):
        self.name = name
        self.lv = lv
        self.skill = '몸통 박치기'
        self.info = name[:2]*2
        Pokemon.population += 1
        self.increase()

    def attack(self):
        return self.skill

    @classmethod
    def increase(cls):
        cls.bell_population += 1

# pika = Pokemon('피카츄')
# print(Pokemon.population)
# print(pika.attack())
# meta = Pokemon('메타몽', lv=5)
# print(meta.attack())
# print(Pokemon.population)
# print(pika.name, pika.lv)
# print(meta.name, meta.lv)
# print(pika.info, meta.info)
