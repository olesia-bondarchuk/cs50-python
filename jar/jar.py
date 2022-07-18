class Jar:
    """
        This class represnt a cookie jar with specified maximum capacity
    """

    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError('Only non-negative number is allowed.')
        self._capacity = capacity
        self._cookies_amount = 0

    def __str__(self):
        result = ''
        for _ in range(self._cookies_amount):
            result += '🍪'
        return result

    def deposit(self, amount_to_deposit):
        if amount_to_deposit <= 0:
            raise ValueError('Invalid amount of cookies to deposit')
        if self._cookies_amount + amount_to_deposit > self._capacity:
            raise ValueError('Too many cookies')

        self._cookies_amount += amount_to_deposit

    def withdraw(self, amount_to_withdraw):
        if amount_to_withdraw <= 0:
            raise ValueError('Invalid amount of cookies to withdraw')
        if self._cookies_amount < amount_to_withdraw:
            raise ValueError('Not enough cookies')

        self._cookies_amount -= amount_to_withdraw

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies_amount
