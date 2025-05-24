from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from pytest import raises
from typing import Dict


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate_with_variance_erro():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(NumpyHandler())
    with raises(Exception) as exc_info:
         calculator_3.calculate(mock_request)

    assert str(exc_info.value) == "Variance is less than multiplication"

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(NumpyHandler())


    response = calculator_3.calculate(mock_request)
    print()
    print(response)

    
