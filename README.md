# Cursor Agent

A Python package for Cursor agent with self-building tools capability.

## Features

- Self-building tool system
- Extensible tool architecture
- Built-in security and validation
- Type-safe implementations

## Installation

```bash
pip install cursor-agent
```

## Usage

```python
from cursor_tools import ToolRegistry

# Initialize the tool registry
registry = ToolRegistry()

# Tools are automatically discovered and registered
tools = registry.get_available_tools()
```

## Development

1. Clone the repository
2. Install development dependencies: `pip install -e ".[dev]"`
3. Create new tools in the `cursor_tools` directory
4. Follow the guidelines in `.cursorrules`

## License

MIT
