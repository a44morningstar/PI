def superset(set1, set2):
    if set1 > set2:
        print(f"Объект {set1} является чистым супермножеством")
    elif set1 == set2:
        print(f"Множества равны")
    elif set2 > set1:
        print(f"Объект {set2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")


if __name__ == "__main__":
    superset({-7, 4, 0, 7, 8, 10, -18, 12, -6}, {12, 13, -1, -18, 17, 3})
