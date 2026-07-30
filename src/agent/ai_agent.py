"""
AI Agent.

This module implements the core AI agent responsible for
interacting with the LLM and executing tools.
"""

import json

from src.groq_client import get_client
from src.schemas.tool_schemas import tools


class Agent:
    """
    AI Agent capable of interacting with the LLM.
    """

    def __init__(self, tool_registry):
        """
        Initialize the AI agent.

        Args:
            tool_registry:
                Registry containing all available tools.
        """

        self.client = get_client()
        self.tool_registry = tool_registry

    def run(self, user_query):
        """
        Process a user query.

        Args:
            user_query:
                User input.

        Returns:
            Tool execution result.
        """

        messages = [
            {
                "role": "user",
                "content": user_query
            }
        ]

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        tool_call = response.choices[0].message.tool_calls[0]

        tool_name = tool_call.function.name

        tool_arguments = json.loads(
            tool_call.function.arguments
        )

        tool = self.tool_registry.get(tool_name)

        tool_result = tool(**tool_arguments)

        return tool_result