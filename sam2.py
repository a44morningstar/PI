def fib(n):
    counter = 0
    a, b = 1, 1
    with open("fib.txt", "a+") as file:
        file.write(str(a) + "\n")
        file.write(str(b) + "\n")
    while counter < n:
        yield (a + b)
        a, b = b, a + b
        counter += 1


if __name__ == "__main__":
    counter = fib(224)
    with open("fib.txt", "a+") as file:
        for i in counter:
            file.write(str(i) + "\n")
