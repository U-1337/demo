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


class CheckingAccount(Account):
    """Банковский счет с комиссией за снятие.

    >>> ch = CheckingAccount('Вася')
    >>> ch.balance = 20
    >>> ch.withdraw(5)
    14
    >>> ch.interest
    0.01
    """

    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_fee)
        # Или же:
        return super().withdraw(amount + self.withdraw_fee)


class Bank:
    """Банк имеет набор счетов и начисляет проценты.

    >>> bank = Bank()
    >>> vasya = bank.open_account('Вася', 10)
    >>> petya = bank.open_account('Петя', 5, CheckingAccount)
    >>> petya.interest
    0.01
    >>> vasya.interest = 0.06
    >>> bank.pay_interest()
    >>> vasya.balance
    10.6
    >>> petya.balance
    5.05
    """
    def __init__(self):
        self.accounts = []

    def open_account(self, holder, amount, account_type=Account):
        """Открывает счет типа account_type для holder с начальным балансом amount."""
        account = account_type(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        """Начисление процентов по всем счетам."""
        for account in self.accounts:
            account.deposit(account.balance * account.interest)


class SavingsAccount(Account):
    """Банковский счет с комиссией за пополнение."""

    deposit_fee = 2

    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_fee)


class AsSeenOnTVAccount(CheckingAccount, SavingsAccount):
    """Банковский счет с комиссиями за всё."""
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 1  # Подарок! Е-е-е!

supers = [c.__name__ for c in AsSeenOnTVAccount.mro()]