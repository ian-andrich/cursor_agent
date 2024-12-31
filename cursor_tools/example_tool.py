from typing import Any, Dict

from .base import BaseTool


class ExampleTool(BaseTool):
    """An example tool that demonstrates the tool structure."""

    def __init__(self):
        super().__init__(
            name="example_tool", description="An example tool that echoes input"
        )

    async def execute(self, **kwargs: Any) -> str:
        """Echo the input message.

        Args:
            message: Message to echo

        Returns:
            str: The echoed message
        """
        message = kwargs.get("message", "")
        return f"Echo: {message}"

    @property
    def parameters(self) -> Dict[str, Dict[str, Any]]:
        """Get parameter specifications.

        Returns:
            Dict[str, Dict[str, Any]]: Parameter specifications
        """
        return {
            "message": {
                "type": "string",
                "description": "Message to echo",
                "required": True,
            }
        }
