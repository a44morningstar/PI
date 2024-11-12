class NegativeValueException(Exception):
    pass


def check_name(name):
    if len(name) > 10:
        raise NegativeValueException("Name is bigger than 10 simbols")
    else:
        print("Successful")


if __name__ == "__main__":
    name = "12345678910"
    check_name(name)
