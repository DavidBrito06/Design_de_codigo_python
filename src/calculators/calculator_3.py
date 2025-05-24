from src.drivers.interfaces.driver_hander_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
        
    def calculate(self, request: FlaskRequest) -> dict:#type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_result(variance, multiplication)

        format_response = self.__format_response(multiplication)
        return format_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise ValueError("Missing 'numbers' in request body")
        

        input_data = body["numbers"]
        return input_data
    

    def __calculate_variance(self,numbers: List[float]) -> float:
        # Example processing: sum of numbers
        variance = self.__driver_handler.variance(numbers)
        return variance
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        # Example processing: sum of numbers
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication
    
    def __verify_result(self, variance: float, multiplication: float) -> None:
        # Example processing: sum of numbers
        if variance <  multiplication:
            raise Exception("Variance is less than multiplication")


    def __format_response(self, variance: float) -> Dict:
        # Format the response
        return {
            "data": {
                "calculator": 3,
                "result": round(variance),
                "success": True

            }
        }
   
        
        
