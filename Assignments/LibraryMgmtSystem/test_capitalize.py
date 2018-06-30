def capital_case(x):

    try:
        res = x.capitalize()
        return res
    except AttributeError as ae:
        return ae

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'
    assert capital_case(123) == AttributeError