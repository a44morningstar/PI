class iceCream:
    def __init__(self, top=None):
        if isinstance(top, str):
            self.top = top
        else:
            self.top = None

    def answer(self):
        if self.top:
            print(f"{self.top} ice cream")
        else:
            print("Plain ice cream")


ic = iceCream()
ic.answer()
ic = iceCream("Cherry")
ic.answer()
ic = iceCream(727)
ic.answer()
