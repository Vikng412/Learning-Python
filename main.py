class Person:
    def __init__(self, x, y, z):
        self.name = x
        self.age = y
        self.health = z
    
    def info(self):
        print(f"{self.name} is a {self.age} years old, with {self.health} pts of health!")


a = Person("Kanishk", "20", "100")
a.info()