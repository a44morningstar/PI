class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


doggo = Dog("Jager", "Rottweiler")
print(f"Welcome, {doggo.name} the {doggo.breed}")
