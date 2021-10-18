import numbers

def test_minimum_input(): 
    '''Tests for input type in minimum function'''
    from functionality.py import minimum()
    assert minimum("string") == nan
