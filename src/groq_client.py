"""
Groq client initialization.

This module is responsible for:
- Validating application configuration
- Creating and returning a Groq client
"""

from groq import Groq

from src.config import Config


def get_client() -> Groq:
    """
    Create and return a configured Groq client.

    Returns:
        Groq:
            Configured Groq client instance.
    """

    Config.validate()

    return Groq(
        api_key=Config.GROQ_API_KEY,
    )