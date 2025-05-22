from .calculator_2 import Calculator2
from typing import Dict

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

   
def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3]})
    calculator_2 = Calculator2()
    format_response =calculator_2.calculate(mock_request)
    print(format_response)