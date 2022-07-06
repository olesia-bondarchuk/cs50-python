from plates import is_valid

def test_is_valid_none_raises_value_error():
    try:
        is_valid(None)
    except ValueError:
        return
    raise AssertionError("ValueError was expected.")

def test_is_valid_wrong_length_returns_false():
    assert is_valid("a") == False
    assert is_valid("abcdefghi") == False

def test_is_valid_does_not_start_with_two_letters_returns_false():
    assert is_valid("b1") == False
    assert is_valid("1a2a") == False

def test_is_valid_does_not_have_only_alphanumeric_symbols_returns_false():
    assert is_valid("bb,1") == False
    assert is_valid("aa!2a") == False

def test_is_valid_first_used_number_cannot_be_zero_returns_false():
    assert is_valid("ad05") == False
    assert is_valid("bc099") == False

def test_is_valid_correct_input_returns_true():
    assert is_valid("ad4560") == True
    assert is_valid("boss") == True

def test_is_valid_letter_after_digit_returns_false():
    assert is_valid("ad05d") == False
    assert is_valid("bc099c") == False