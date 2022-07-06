from fuel import convert, gauge

def test_convert_wrong_format_raises_value_error():
    try:
        convert("1")
    except ValueError:
        return 
    raise AssertionError("ValueError was expected.")

def test_convert_first_argument_not_a_digit_raises_value_error():
    try:
        convert("cat/10")
    except ValueError:
        return 
    raise AssertionError("ValueError was expected.")

def test_convert_second_argument_not_a_digit_raises_value_error():
    try:
        convert("2/dog")
    except ValueError:
        return 
    raise AssertionError("ValueError was expected.")

def test_convert_first_argument_greater_than_second_argument_raises_value_error():
    try:
        convert("3/1")
    except ValueError:
        return 
    raise AssertionError("ValueError was expected.")

def test_convert_second_argument_equals_zero_raises_zeroDivision_error():
    try:
        convert("3/0")
    except ZeroDivisionError:
        return 
    raise AssertionError("ZeroDevisionError was expected.")

def test_gauge_returns_E():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"

def test_gauge_returns_F():
    assert gauge(99) == "F"

def test_gauge_wrong_percentage_returns_value_error():
    try:
        gauge(111) 
    except ValueError:
        return
    raise AssertionError("Persentage cannot be less than 0 or greater than 100.")
    

def test_gauge_returns_percent():
    assert gauge(70) == "70%"
    assert gauge(5) == "5%"