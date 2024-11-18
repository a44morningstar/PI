def fib(n):
    counter = 0
    a, b = 1, 1
    print(1)
    print(1)
    while counter < n:
        yield (a + b)
        a, b = b, a + b
        counter += 1


if __name__ == "__main__":
    counter = fib(224)
    for i in counter:
        print(i)
