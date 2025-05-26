from src.drivers.interfaces.driver_hander_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.http_unprocessable_entity import UnprocessableEntityError


class Calculator4:
    def __init__(self, driver_handler):
        self.__driver_handler = driver_handler

    def calculate(self, request):
        body = request.json
        input_data = self.__validate_body(body)
        median_result = self.process_median(input_data)
        return self.__format_response(median_result)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise UnprocessableEntityError("Missing 'numbers' in request body")

        input_data = body["numbers"]
        return input_data

    def process_median(self, input_data):
        return self.__driver_handler.median(input_data)

    def __format_response(self, calc_result):
        return {
            "data": {
                "calculator": 4,
                "result": round(calc_result, 2)
            }
        }

