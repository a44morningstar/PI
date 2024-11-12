def check(input_func):
    def output_func(*args):
        name, age = (
            args[0],
            args[1],
        )

        if age < 0 or age > 130:
            age = "Wrong input"
        input_func(name, age)

    return output_func


@check
def personal_info(name, age):
    print(f"Name: {name} Age: {age}")


if __name__ == "__main__":
    personal_info("Tom", 52)
    personal_info("Rudy", -1)
    personal_info("Lora", 131, 0, 4, 5)
