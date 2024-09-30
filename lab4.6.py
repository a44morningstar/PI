def main(**kwargs):
    for i, j in kwargs.items():
        print(f"{i}={srAr(j)}")


def srAr(inf):
    return sum(inf) / len(inf)


if __name__ == "__main__":
    main(
        a=[59, 39, 27, 53],
        b=[40, 29, 17],
        c=[57, 4, 80, 78, 64, 13, 46, 71],
        d=[100, 3, 77, 82, 2],
    )
