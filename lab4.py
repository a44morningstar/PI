class Mammal:
    animalClass = "Mammal"


class Dog(Mammal):
    family = "Canine"
    species = "Dog"


class Cat(Mammal):
    family = "Feline"
    species = "Cat"


print(
    f"Dogs are belong to class {Dog().animalClass}s, family {Dog().family}s and species {Dog().species}s"
)
print(
    f"Cats are belong to class {Cat().animalClass}s, family {Cat().family}s and species {Cat().species}s"
)
