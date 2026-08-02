"""
Agent Builder.

Responsible for creating a fully configured AI Agent.
"""

from src.agent.ai_agent import Agent
from src.config import Config
from src.schemas.tool_schemas import tools
from src.tool_registry import ToolRegistry

from src.tools.calculator import calculator
from src.tools.weather import weather
from src.tools.current_time import current_time


def build_agent():
    """
    Build and return a configured AI Agent.

    Returns:
        Agent:
            Configured AI Agent.
    """

    registry = ToolRegistry()

    registry.register(
        "calculator",
        calculator,
    )

    registry.register(
        "weather",
        weather,
    )

    registry.register(
        "current_time",
        current_time,
    )

    return Agent(
        tool_registry=registry,
        tool_schemas=tools,
        model=Config.MODEL_NAME,
    )