from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self._json = body

    def get_json(self):
        return self._json

def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    print(response)

    #formato da resposta
    assert "data" in response
    assert "calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["calculator"] == 1
    assert response["data"]["result"] == 14.25


def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request)
    
    assert str(excinfo.value) == "body mal formado!"
  

    
