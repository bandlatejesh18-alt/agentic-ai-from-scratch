"""
Current Time tool.

This module retrieves the current date and time
from the local system.
"""

from datetime import datetime


def current_time():
    """
    Retrieve the current date and time.

    Returns:
        A dictionary containing the current date and time
        or an error message.
    """

    try:

        now = datetime.now()

        return {
            "success": True,
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S")
        }

    except Exception as error:

        return {
            "success": False,
            "error": str(error)
        }