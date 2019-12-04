class Clown:
    """Демонстрация инструкции class. Этот класс бесполезен.

    >>> Clown.nose
    'большой и красный'
    >>> Clown.dance()
    'Спасибо, не надо!'
    """
    nose = 'большой и красный'
    def dance():
        return 'Спасибо, не надо!'


class Account:
    """Счет включает баланс (balance) и держателя (holder).
    Все счета имеют общую ставку (interest).

    >>> a = Account('Вася')
    >>> a.holder
    'Вася'
    >>> a.deposit(100)
    100
    >>> a.withdraw(90)
    10
    >>> a.withdraw(90)
    'Недостаточно средств'
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> Account.interest = 0.04
    >>> a.interest
    0.04
    """

    interest = 0.02  # Аттрибут класса

    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        """Положить деньги на счет."""
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        """Снять деньги со счета, если это возможно."""
        if amount > self.balance:
            return 'Недостаточно средств'
        self.balance = self.balance - amount
        return self.balance