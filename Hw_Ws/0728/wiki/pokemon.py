class Pokemon:
    info = '푸키먼'
    population = 0
    bell_population = 0
    def __init__(self, name, lv=1):
        self.name= name
        self.lv= lv
        self.skill = '몸통 박치기'
        self.info = name[:2]*2
        Pokemon.population+= 1
        self.increase()
    def attack(self):
        return self.skill

    @classmethod
    def increase(cls):
        cls.bell_population +=1

# pika = Pokemon('피카츄')
# print(Pokemon.population)
# meta = Pokemon('메타몽',lv=5)
# print(Pokemon.population)

# print(pika.name, pika.lv)
# print(meta.name, meta.lv)
# print(pika.info, meta.info)
