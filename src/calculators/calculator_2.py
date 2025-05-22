from flask import request as FlaskRequest
from typing import Dict, List

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict:#type: ignore[no-untyped-def]
        body = request.json
        print(body)
        input_data = self.__validate_body(body)
        print(input_data)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise ValueError("Missing 'numbers' in request body")
        

        input_data = body["numbers"]
        return input_data
    