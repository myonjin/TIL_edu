from cmath import pi
from wiki.pokemon import Pokemon


class pikatchu(Pokemon):
    no = 25
    population = 0
    
    def __init__(self, name ,lv=5):
        super().__init__(name, lv)
        self.skill ='전기 충격'

    def attack(self):
        return '찌릿 찌릿'
    
    def walk():
        return '뚜벅 뚜벅'

class metamong(Pokemon):
    no = 132

    def __init__(self, name, lv=1):
        super().__init__(name, lv)
        self.skill = '변신'
    
    def attack(self):
        return '메타 메타'
        
    def eat(self):
        return '냠'

class Child(pikatchu, metamong):
    pass


ch = Child('메타몽')

class Brother(metamong,pikatchu):
    pass
br = Brother('메타몽')
print(ch.name)
print(ch.skill)
print(ch.attack())
# print(ch.eat())

print(pikatchu.bell_population)
print(metamong.bell_population)
print(Child.bell_population)

# pika = pikatchu('피카츄')
# print(pika.info)
# print(pika.skill)
# print(Pokemon.bell_population)
# print(pikatchu.bell_population)


# meta = metamong('메타몽')

# print(meta.info)
# print(metamong.bell_population)