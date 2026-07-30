from src.agent.ai_agent import Agent
from src.tool_registry import ToolRegistry

from src.tools.calculator import calculator
from src.tools.weather import weather
from src.tools.current_time import current_time


def main():

    registry = ToolRegistry()

    registry.register("calculator", calculator)
    registry.register("weather", weather)
    registry.register("current_time", current_time)

    agent = Agent(registry)

    response = agent.run(
        "What is the weather in Hyderabad?"
    )

    print(response)


if __name__ == "__main__":
    main()