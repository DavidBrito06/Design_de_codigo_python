from .calculator_4 import Calculator4
from pytest import raises
from typing import Dict, List
from src.calculators.calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: dict):
        self.json = body

class MockDriverHandler:
    def median(self, numbers: list[float]) -> float:
        return sorted(numbers)[len(numbers)//2]

def test_calculate_median():

    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator = Calculator4(MockDriverHandler())
    response = calculator.calculate4(mock_request)

    print(response)
    assert response["data"]["result"] == 3


