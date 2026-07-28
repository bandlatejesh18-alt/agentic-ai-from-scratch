"""
Calculator tool.

This module provides a calculator tool that evaluates
simple mathematical expressions.
"""


def calculator(expression):
    """
    Evaluate a mathematical expression.

    Args:
        expression:
            Mathematical expression as a string.

    Returns:
        A dictionary containing the calculation result
        or an error message.
    """

    try:
        result = eval(expression)

        return {
            "success": True,
            "result": result
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }