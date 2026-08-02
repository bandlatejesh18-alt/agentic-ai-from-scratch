from src.agent.ai_agent import Agent
from src.tool_registry import ToolRegistry
from src.config import Config
from src.schemas.tool_schemas import tools

from src.tools.calculator import calculator
from src.tools.weather import weather
from src.tools.current_time import current_time


def main():

    registry = ToolRegistry()

    registry.register("calculator", calculator)
    registry.register("weather", weather)
    registry.register("current_time", current_time)

    agent = Agent(
        tool_registry=registry,
        tool_schemas=tools,
        model=Config.MODEL_NAME,
    )

    response = agent.run(
        "What is the current temperature in hyderabad and current time and temperature multipled by 10?"
    )

    print(response)


if __name__ == "__main__":
    main()