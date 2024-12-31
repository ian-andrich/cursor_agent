from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseTool(ABC):
    """Base class for all Cursor tools."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
    @abstractmethod
    async def execute(self, **kwargs: Any) -> Any:
        """Execute the tool's main functionality.
        
        Args:
            **kwargs: Tool-specific arguments
            
        Returns:
            Any: Tool-specific return value
        """
        pass
    
    @property
    @abstractmethod
    def parameters(self) -> Dict[str, Dict[str, Any]]:
        """Get the tool's parameter specifications.
        
        Returns:
            Dict[str, Dict[str, Any]]: Parameter specifications
        """
        pass
    
    def validate_params(self, params: Dict[str, Any]) -> Optional[str]:
        """Validate the provided parameters.
        
        Args:
            params: Parameters to validate
            
        Returns:
            Optional[str]: Error message if validation fails, None otherwise
        """
        required_params = {
            name for name, spec in self.parameters.items()
            if spec.get("required", False)
        }
        
        missing = required_params - params.keys()
        if missing:
            return f"Missing required parameters: {', '.join(missing)}"
        
        return None 