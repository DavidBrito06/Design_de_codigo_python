from .http_unprocessable_entity import UnprocessableEntityError
from .http_bad_request import HttpBadRequestError
from typing import Dict

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (UnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [
                    {
                        "message": error.message,
                        "name": error.name,
                    }
                ]
            }
        }
    return {
        "status_code": 500,
        "body": {
            "errors": [
                {
                    "message": "Internal Server Error",
                    "name": "InternalServerError",
                }
            ]
        }
    }
