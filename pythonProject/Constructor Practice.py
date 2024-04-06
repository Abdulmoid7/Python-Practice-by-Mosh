class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


Abdul_Moid_Siddique = Person("Abdul Moid Siddique")
print(Abdul_Moid_Siddique.name)
Abdul_Moid_Siddique.talk()

Ali = Person("Ali Khan")
Ali.talk()