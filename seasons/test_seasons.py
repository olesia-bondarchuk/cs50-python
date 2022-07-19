from seasons import difference_between_two_dates_in_minutes

def test_difference_between_two_dates_in_minutes_has_correcy_parametr_length():
    try:
        difference_between_two_dates_in_minutes('1990')
    except ValueError:
        pass
    else:
        raise AssertionError('ValueError was expected')

    try:
        difference_between_two_dates_in_minutes('1990-1')
    except ValueError:
        return
    raise AssertionError('ValueError was expected')

def test_difference_between_two_dates_in_minutes_raises_error_if_parametr_is_not_int():
    try:
        difference_between_two_dates_in_minutes('cat')
    except ValueError:
        return
    raise AssertionError('ValueError was expected')
