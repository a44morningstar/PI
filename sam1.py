import time


def fib():
    fib1 = fib2 = 1

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=" ")


if __name__ == "__main__":
    a = time.time()
    fib()
    b = time.time()
    print(f"\nПрограмма выполнялась {int((b - a) * 1000)} миллисекунд")
