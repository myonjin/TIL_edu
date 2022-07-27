class doggy:
    
    count=0
    num_of_dogs=5
    birth_of_dogs=5

    def __init__(self,name,breed):
        self.name =name
        self.breed= breed
        

    def talk(self):
        print('멍')
    
    def get_status(self):
        print(birth_of_dogs,num_of_dogs)

t1= doggy()
t1.get_status()

dog = doggy('siba')
print(dog.name)

