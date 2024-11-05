class Ana:
    __slots__ = ["name"]

    def __init__(self, name):
        if name == "Ana":
            self.name = f"Yes, I'm {name}"
        else:
            self.name = f"No, I'm not {name}, I'm Ana"


print(Ana("Diana").name)
print(Ana("Ana").name)
