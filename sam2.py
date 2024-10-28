class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("woof woof")

    def pat(self):
        print(f"{self.name} loves pets!")


doggo = Dog("Jager", "Rottweiler")
print(f"Welcome, {doggo.name} the {doggo.breed}")
doggo.pat()
doggo.bark()
