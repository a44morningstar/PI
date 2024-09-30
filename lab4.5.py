def main(**kwargs):
    for i in kwargs.items():
        print(i[0], "=", i[1])


if __name__ == "__main__":
    main(a=[9, 10, 5], b=[5, 7, 2], c=[4, 3, 2], d=[3, 9, 9])
