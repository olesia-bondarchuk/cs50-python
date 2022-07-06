from working import twelve_to_twenty_four_format, convert

def test_twelve_to_twenty_four_format_invalid_hours_and_minutes_trows_values_error():
    try:
       twelve_to_twenty_four_format("13", "60", "AM")
    except ValueError:
        return 

    raise AssertionError("ValueError was expected")


def test_twelve_to_twenty_four_format_none_minutes_returns_00():
    assert twelve_to_twenty_four_format("12", "", "PM") == "24:00"
    

def test_twelve_to_twenty_four_format_does_the_change():
    assert twelve_to_twenty_four_format("11", "10", "PM") == "23:10"

def test_twelve_to_twenty_four_format_adds_zero_to_minutes():
    assert twelve_to_twenty_four_format("5", "5", "AM") == "5:05"

def test_convert_invalid_input_raises_value_error():
    try:
       convert("6:40 am")
    except ValueError:
        return 

    raise AssertionError("ValueError was expected")

    try:
       convert("15:40 AM")
    except ValueError:
        return 

    raise AssertionError("ValueError was expected")

    try:
       convert("2:61 PM")
    except ValueError:
        return 

    raise AssertionError("ValueError was expected")

def test_convert_returns_correct_result():
    assert convert("2 AM to 5 PM") == "2:00 to 17:00"
    assert convert("12:10 AM to 7:30 PM") == "12:10 to 19:30"
    assert convert("4 PM to 3:20 PM") == "16:00 to 15:20"