from wiki.pokemon import Pokemon

class Pikatchu(Pokemon):
    no = 25

    def __init__(self, name, lv=5):
        # 내 직속 상속 부모가 가진 메서드 호출하기
        # 호출할 때, 인자 넘겨주기
        super().__init__(name, lv)
        self.skill = '전기 충격'

    def attack(self):
        return '찌릿 찌릿'

    def walk():
        return '뚜벅 뚜벅'


class Metamong(Pokemon):
    no = 132

    def __init__(self, name, lv=1):
        super().__init__(name, lv)
        self.skill = '변신'

    def attack(self):
        return '메타 메타'

    def eat(self):
        return '냠냠'

class Child(Pikatchu, Metamong):
    pass

class Brother(Metamong, Pikatchu):
    pass

br = Brother('메타몽')
print(br.name)
print(br.skill)
print(br.attack())

# ch = Child('메타몽')
# print(ch.name)
# print(ch.skill)
# print(ch.attack())
# print(ch.eat())
# print(Pikatchu.bell_population)
# print(Metamong.bell_population)
# print(Child.bell_population)
  
# pika = Pikatchu('피카츄')
# print(pika.info)
# print(pika.skill)
# print(Pokemon.population)
# print(Pikatchu.bell_population)

# meta = Metamong('메타몽')
# print(Pokemon.population)
# print(Pikatchu.bell_population, '피카츄')
# print(Metamong.bell_population, '메타몽')
# print(meta.info)