class Being:

    kingdom = "Not specified"

    def add(a, b):
        return a + b

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("Usuwam obiekt klasy: ", type(self).__name__)

    def greet(self):
        print (f"Hello, I am {self.name} of Kingdom of {self.kingdom}")

class Animal(Being):

    kingdom = "Animals"

    def __init__(self, name, age, weight):
        super().__init__(name)
        self.age = int(age)
        self.weight = int(weight)

    def greet(self):
        print (f"Hello, I am {self.name} of Kingdom of {self.kingdom}")

class Cat(Animal):

    def greet(self):
        print("Meow, i am a cat: ", self.name)

me = Being("Being")
me.greet()

me = Animal("Abc", 1 , 5)
me.greet()

me = Cat("Borubar", 2, 5)
me.greet()