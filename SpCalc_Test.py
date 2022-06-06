"""
Test Application
"""
import SpCalc


# need to mock the
def test_special_calc(mocker):
    """Special Calculator Test"""
    mock_now = mocker.patch("SpCalc.random")
    mock_now.randint.return_value = 2
    specimen = 6
    output = SpCalc.special_calc(specimen)
    expected = specimen + 2

    assert expected == output


# https://docs.python.org/3/library/unittest.mock-examples.html

# real = ProductionClass()
# real.something = MagicMock()
# real.method()
# real.something.assert_called_once_with(1, 2, 3)
