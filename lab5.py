class Russian:
    @staticmethod
    def greeting():
        print("Привет")


class English:
    @staticmethod
    def greeting():
        print("Hello")


class Spanish:
    @staticmethod
    def greeting():
        print("Hola")


def greet(lang):
    lang.greeting()


Ana = Russian()
Tom = English()
Juan = Spanish()
greet(Ana)
greet(Tom)
greet(Juan)
