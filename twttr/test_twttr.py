from xmlrpc.client import ResponseError
from twttr import shorten

def test_shorten_empty_string_throws_value_error():
    try:
        shorten("")
    except ValueError:
        return 

    raise AssertionError("ValueError was expected")

def test_shorten_none_throws_value_error():
    try:
        shorten(None)
    except ValueError:
        return 

    raise AssertionError("ValueError was expected")

def test_shorten_empty_result_throws_response_error():
    try:
        shorten("aoiue")
    except ResponseError:
        return 

    raise AssertionError("ResponseError was expected")

def test_shorten_removes_vowels():
    assert shorten("CATDOGmiceduck123!,.") == "CTDGmcdck123!,."