class Being:

    kingdom = "Not specified"

    def __init__(self, name = "Not specified"):
        self.name = name

    def greet(self):
        print (f"Hello, I am {self.name} of Kingdom of {self.kingdom}")

me0 = Being()
me0.greet()

class Animal(Being):

    def __init__(self, name):
        super().__init__(name)
        self.kingdom = "Animal"

me = Being("cat")
me.greet()

me2 = Animal("parrot")
me2.greet()