class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1

    def bark(self):
        return '왈왈!'

    @classmethod
    def get_status(cls):
        return f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}'
