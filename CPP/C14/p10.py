# Single inheritance example
class Bank(object):
    cash = 1000000

    @classmethod
    def available_cash(cls):
        print(cls.cash)


class AndhraBank(Bank):
    pass


class StateBank(Bank):
    cash = 2000000

    @classmethod
    def available_cash(cls):
        print(cls.cash + Bank.cash)


a = AndhraBank()
a.available_cash()

s = StateBank()
s.available_cash()