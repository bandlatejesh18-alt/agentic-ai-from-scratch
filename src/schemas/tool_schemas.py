calculator_schema = {
    "type": "function",
    "function": {
        "name": "calculator",
        "description": "Evaluate a mathematical expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "The mathematical expression to evaluate."
                }
            },
            "required": ["expression"]
        }
    }
}


weather_schema = {
    "type": "function",
    "function": {
        "name": "weather",
        "description": "Retrieve the current temperature for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "City name."
                }
            },
            "required": ["city"]
        }
    }
}


current_time_schema = {
    "type": "function",
    "function": {
        "name": "current_time",
        "description": "Retrieve the current local date and time.",
        "parameters": {
            "type": "object",
            "properties": {}
        }
    }
}


tools = [
    calculator_schema,
    weather_schema,
    current_time_schema
]