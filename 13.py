def make_withdraw(balance):
    """Возвращает функцию withdraw с начальным балансом."""
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Недостаточно средств'
        balance = balance - amount
        return balance
    return withdraw

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]:
            return 'Недостаточно средств'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x + 1
            return x + y + z
        return h
    return g
a = f(1)
b = a(2)
b(3) + b(4)

def king(arthur):
    def sir(galahad):
        nonlocal arthur
        if arthur(galahad) == 0:
            return [galahad+1, galahad-1]
        arthur = lambda pure: galahad-pure
        return [galahad, sir(galahad)]
    return sir(2)
king(abs)
