def inf(name, age, company="not stated"):
    print(f"Имя - {name}, возраст - {age}, комнапиня - {company}")


p1 = ("Thomas", 25)
p2 = ("Alexander", 33, "Oriflame")
inf(*p1)
inf(*p2)
