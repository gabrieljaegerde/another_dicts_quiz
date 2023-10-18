from solutions.dicts import get_length, update_value

def test_get_length():
    assert get_length({'a': 1, 'b': 2}) == 2

def test_update_value():
    assert update_value({'a': 1, 'b': 2}, 'a', 3) == {'a': 3, 'b': 2}

