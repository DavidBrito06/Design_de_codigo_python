from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict:#type: ignore[no-untyped-def]
        body = request.json
        input_data = self.__validate_body(body)
        self.__process_data(input_data)
       

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise ValueError("Missing 'numbers' in request body")
        

        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        # Example processing: sum of numbers
        numpy_handler = NumpyHandler()
        first_process_result  = [(num *11) ** 0.95 for num in input_data]
        print(first_process_result)
        result =numpy_handler.standard_derivation(first_process_result)
        print(result)
        return 1/result
        

    
