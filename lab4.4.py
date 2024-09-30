def main(a, b, *args):
    x = sum(args)
    y = a * b
    print(f"{x}\n{y}")
    return x / float(len(args))


if __name__ == "__main__":
    res = main(42, 50, 15, 8, 24, 2, 21, 24, 48, 8, 1, 33, 35, 30, 20)
    print(res)
