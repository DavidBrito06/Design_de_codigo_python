from .calculator_2 import Calculator2
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    def standard_derivation(self, numbers: List[float]) -> float:
        # Mock implementation of standard_derivation
        return 3


def test_calculate_integration():
    mock_request = MockRequest({"numbers": [1, 2, 3]})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    format_response =calculator_2.calculate(mock_request)
    print(format_response)

    assert isinstance(format_response, dict)
    assert format_response == {'data': {'calculator': 2, 'result': 0.14}}



def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3]})
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    format_response =calculator_2.calculate(mock_request)
    print(format_response)

    assert isinstance(format_response, dict)
    assert format_response == {'data': {'calculator': 2, 'result': 0.33}}