from src.groq_client import get_client
from src.tool_registry import ToolRegistry

from src.tools.calculator import calculator
from src.tools.weather import weather
from src.tools.current_time import current_time

def main():
    
    client = get_client()

    registry = ToolRegistry()

    registry.register(
        "calculator",
        calculator
    )
    
    registry.register(
        "weather",
        weather
    )
    
    registry.register(
        "current_time",
        current_time
    )

    calculator_tool = registry.get("calculator")
    print(calculator_tool("25*19"))
    
    weather_tool = registry.get("weather")
    print(weather_tool("Hyderabad"))
    
    time_tool = registry.get("current_time")
    print(time_tool())


if __name__ == "__main__":
    main()