fout = list()
for st in open("input.txt", "r", encoding="utf-8"):
    intAge = int(st.split()[1])
    if intAge < 40:
        fout.append(st)
print(fout)
