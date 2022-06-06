"""
Test Application
"""
import pytest

import SpCalc


# patching
def test_special_calc(mocker):
    """Special Calculator Test"""
    mock_now = mocker.patch("SpCalc.random")
    mock_now.randint.return_value = 2
    specimen = 6
    output = SpCalc.special_calc(specimen)
    expected = specimen + 2

    assert expected == output

#parametrized patching
@pytest.mark.parametrize(
    "rand, expect",
    [
        (2, 8),
        (5, 11),
        (89, 95),
        (1, 7),
        (7, 13),
        (14, 20),
        (12, 18),
    ],
)
def test_get_time_of_day(rand, expect, mocker):
    """Special Calculator Test"""
    mock_now = mocker.patch("SpCalc.random")
    mock_now.randint.return_value = rand
    specimen = 6
    output = SpCalc.special_calc(specimen)
    expected = specimen + rand

    assert expected == output

# https://docs.python.org/3/library/unittest.mock-examples.html

# real = ProductionClass()
# real.something = MagicMock()
# real.method()
# real.something.assert_called_once_with(1, 2, 3)
