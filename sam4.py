class Dog:
    def __init__(self, name, breed):
        self.__name = name
        self._breed = breed

    def bark(self):
        print("woof woof")

    def pat(self):
        print("Dogs love pets!")


class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


class CompanionDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


doggo1 = GuardDog("Jager", "Rottweiler")
doggo2 = CompanionDog("Willow", "Golden Retriever")
doggo1.pat()
print(f"Welcome, the {doggo1._breed}")
print(f"Welcome, the {doggo2._breed}")
