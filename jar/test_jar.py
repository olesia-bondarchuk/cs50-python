from jar import Jar


def test_init_negative_capacity_raises_value_error():
    try:
        Jar(-1)
    except ValueError:
        return
    raise AssertionError('ValueError was expected')

def test_init_zero_capacity_raises_value_error():
    try:
        Jar(0)
    except ValueError:
        return
    raise AssertionError('ValueError was expected')

def test_init_correct_capacity_works_properly():
    jar = Jar(2)
    assert jar.capacity == 2
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



def test_deposit_negative_amount_of_cookies_to_deposit_raises_valueerror():
    jar = Jar()
    try:
        jar.deposit(-1)
    except ValueError:
        return
    raise AssertionError('ValueError was expected')

def test_deposit_too_many_cookies_raises_valueerror():
    jar = Jar(5)
    jar.deposit(3)
    try:
        jar.deposit(3)
    except ValueError:
        return
    raise AssertionError('ValueError was expected')

def test_deposit_works_properly():
    jar = Jar(10)
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(5)
    assert jar.size == 6
    jar.deposit(4)
    assert jar.size == 10
    assert jar.capacity == 10

def test_withdraw_negative_amount_of_cookies_to_withdraw_raises_valueerror():
    jar = Jar()
    try:
        jar.withdraw(-1)
    except ValueError:
        return
    raise AssertionError('ValueError was expected')

def test_withdraw_too_many_cookies_raises_valueerror():
    jar = Jar(5)
    try:
        jar.withdraw(1)
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError was expected')

    jar.deposit(1)

    try:
        jar.withdraw(2)
    except ValueError:
        return
    raise AssertionError('ValueError was expected')

def test_withdraw_works_properly():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1
    jar.withdraw(1)
    assert jar.size == 0
    assert jar.capacity == 10
