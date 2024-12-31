import importlib
import inspect
import pkgutil
from typing import Dict, List

from .base import BaseTool


class ToolRegistry:
    """Registry for managing and discovering Cursor tools."""
    
    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}
        
    def register_tool(self, tool: BaseTool) -> None:
        """Register a new tool.
        
        Args:
            tool: Tool instance to register
        """
        self._tools[tool.name] = tool
        
    def get_tool(self, name: str) -> BaseTool:
        """Get a tool by name.
        
        Args:
            name: Name of the tool
            
        Returns:
            BaseTool: The requested tool
            
        Raises:
            KeyError: If tool doesn't exist
        """
        return self._tools[name]
        
    def get_available_tools(self) -> List[BaseTool]:
        """Get all registered tools.
        
        Returns:
            List[BaseTool]: List of available tools
        """
        return list(self._tools.values())
        
    def discover_tools(self, package_name: str = "cursor_tools") -> None:
        """Discover and register tools from a package.
        
        Args:
            package_name: Package to search for tools
        """
        package = importlib.import_module(package_name)
        
        for _, name, is_pkg in pkgutil.iter_modules(package.__path__):
            if not is_pkg:
                module = importlib.import_module(f"{package_name}.{name}")
                for _, obj in inspect.getmembers(module):
                    if (inspect.isclass(obj) and 
                            issubclass(obj, BaseTool) and 
                            obj != BaseTool):
                        self.register_tool(obj()) 