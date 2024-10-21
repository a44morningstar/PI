with open("input1.txt", "a+") as file:
    file.write(
        "\nNo ore takes better to being forged than the infernal iron of Avernus, where the archdevil Zariel presides."
    )

with open("input1.txt", "r") as file:
    print(file.readlines())
