class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        if self._successor:
            return self._successor.handle(request)
        return None


class Dispenser1000(Handler):
    def handle(self, request):
        if request >= 1000:
            num = request // 1000
            remainder = request % 1000
            print(f"Dispensing {num} x 1000 AMD")
            if remainder != 0:
                return super().handle(remainder)
        else:
            return super().handle(request)


class Dispenser500(Handler):
    def handle(self, request):
        if request >= 500:
            num = request // 500
            remainder = request % 500
            print(f"Dispensing {num} x 500 AMD")
            if remainder != 0:
                return super().handle(remainder)
        else:
            return super().handle(request)


class Dispenser100(Handler):
    def handle(self, request):
        if request >= 100:
            num = request // 100
            remainder = request % 100
            print(f"Dispensing {num} x 100 AMD")
            if remainder != 0:
                return super().handle(remainder)
        else:
            return super().handle(request)


class ATM:
    def __init__(self):
        self.chain = Dispenser1000(Dispenser500(Dispenser100()))

    def dispense(self, amount):
        self.chain.handle(amount)


# Пример использования
atm = ATM()
atm.dispense(3600)  # Output: Dispensing 3 x 1000 AMD, Dispensing 1 x 500 AMD, Dispensing 1 x 100 AMD
