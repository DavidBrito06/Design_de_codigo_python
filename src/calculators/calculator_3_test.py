from .calculator_3 import Calculator3
from pytest import raises
from typing import Dict, List


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        # Mock implementation of variance
        return 3

class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        # Mock implementation of variance
        return 1000000

def test_calculate_with_variance_erro():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())
    with raises(Exception) as exc_info:
         calculator_3.calculate(mock_request)

    assert str(exc_info.value) == "Variance is less than multiplication"

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())


    response = calculator_3.calculate(mock_request)
    print()
    print(response)

    assert response == {'data': {'calculator': 3, 'result': 1000000, 'success': True}}

    
