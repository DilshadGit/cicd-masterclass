"""REST API endpoints for the microservice"""
from http import HTTPStatus
from typing import Dict, Any

def health_check() -> Dict[str, Any]:
    return {
        "status": "healthy",
        "service": "teachcloud-cicd-service",
        "version": "1.0.0"
    }

def process_calculation(op: str, a: float, b: float) -> Dict[str, Any]:
    from .calculator import add, subtract, multiply, divide
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }
    if op not in operations:
        return {"error": f"Unsupported operation: {op}", "status": HTTPStatus.BAD_REQUEST}
    try:
        result = operations[op](a, b)
        return {"operation": op, "a": a, "b": b, "result": result, "status": HTTPStatus.OK}
    except ValueError as e:
        return {"error": str(e), "status": HTTPStatus.UNPROCESSABLE_ENTITY}
