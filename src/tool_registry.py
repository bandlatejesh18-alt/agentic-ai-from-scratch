"""
Tool registry for managing agent tools.

This module stores and retrieves tools that the AI agent can use.
Instead of writing multiple if-else statements, the agent can
retrieve a tool using its name.
"""


class ToolRegistry:
    """
    Stores and manages all available tools.
    """

    def __init__(self):
        """
        Initialize an empty tool registry.
        """

        self.tools = {}

    def register(self, name, tool):
        """
        Register a tool in the registry.

        Args:
            name:
                Name of the tool.

            tool:
                Function implementing the tool.

        Returns:
            None
        """

        self.tools[name] = tool

    def get(self, name):
        """
        Retrieve a tool from the registry.

        Args:
            name:
                Name of the tool.

        Returns:
            The registered tool if it exists.
            Otherwise, returns None.
        """

        return self.tools.get(name)

    def list_tools(self):
        """
        Return the names of all registered tools.

        Args:
            None

        Returns:
            A list containing the names of all registered tools.
        """

        return list(self.tools.keys())