from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_hander_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import UnprocessableEntityError

class Calculator2:
    def __init__(self,driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:#type: ignore[no-untyped-def]
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)

        format_response = self.__format_response(calculated_number)
        return format_response

       

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise UnprocessableEntityError("Missing 'numbers' in request body")

        input_data = body["numbers"]
        return input_data
    
    def __process_data(self, input_data: List[float]) -> float:
        # Example processing: sum of numbers
    
        first_process_result  = [(num *11) ** 0.95 for num in input_data]

        result =self.__driver_handler.standard_derivation(first_process_result)

        return 1/result
    

    def __format_response(self, calc_result: float) -> Dict:
        # Format the response
        return {
            "data": {
                "calculator": 2,
                "result": round(calc_result, 2)
            }
        }
   
        

    
