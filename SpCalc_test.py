import random

import SpCalc

# need to mock the
def special_calc_test():
    x = 6
    expected = SpCalc.special_calc(x)
    output = x + random.randint(1,5)
    assert expected == output

# https://docs.python.org/3/library/unittest.mock-examples.html

#real = ProductionClass()
#real.something = MagicMock()
#real.method()
#real.something.assert_called_once_with(1, 2, 3)