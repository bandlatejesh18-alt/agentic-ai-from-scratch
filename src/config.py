"""
Configuration management for the Agentic AI project.

This module is responsible for:
- Loading environment variables
- Validating required configuration
- Providing centralized access to configuration values
"""

import os

from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()


class Config:
    """
    Centralized application configuration.

    This class loads all configuration values from environment
    variables and provides a single place to access them.
    """

    # ==================================================
    # Groq Configuration
    # ==================================================

    GROQ_API_KEY: str | None = os.getenv("GROQ_API_KEY")

    # ==================================================
    # Model Configuration
    # ==================================================

    MODEL_NAME: str = os.getenv(
        "MODEL_NAME",
        "llama-3.3-70b-versatile",
    )

    @classmethod
    def validate(cls) -> None:
        """
        Validate that all required configuration values are present.

        Raises:
            ValueError:
                If a required configuration value is missing.
        """

        if cls.GROQ_API_KEY is None:
            raise ValueError(
                "Missing GROQ_API_KEY.\n"
                "Please create a '.env' file from '.env.example' "
                "and add your Groq API key."
            )