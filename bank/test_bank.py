from bank import value

def test_value_empty_string_throws_value_error():
    try:
        value("")
    except ValueError:
        return 
    raise AssertionError("ValueError was expected.")

def test_value_none_throws_value_error():
    try:
        value(None)
    except ValueError:
        return 
    raise AssertionError("ValueError was expected.")

def test_value_returns_zero():
    assert value("hello") == 0
    assert value("hello, Dima") == 0

def test_value_returns_twenty():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("help") == 20
    assert value("hell") == 20

def test_value_returns_hundred():
    assert value("cat") == 100
    assert value("welcome") == 100
    assert value("enjoy") == 100




