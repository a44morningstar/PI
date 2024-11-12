def data(*args):
    try:
        for i in range(len(*args)):
            try:
                result = (args[0][i] * 15) // 10
                print(result)
            except Exception as ex:
                print(ex)
    except Exception as e:
        print(e)
    finally:
        print("Information has been processed")


if __name__ == "__main__":
    data([10, -1, "Grgr", "Monkey", "f", "low", 100])
