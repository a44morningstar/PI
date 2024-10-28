class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

    def pat(self):
        print(f"{self.name} loves pets!")


class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


class CompanionDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)


doggo1 = GuardDog("Jager", "Rottweiler")
doggo2 = CompanionDog("Willow", "Golden Retriever")
doggo1.bark()
doggo2.pat()
