"""CLI interface for cursor tools."""
import asyncio
from typing import Optional

import click
from rich.console import Console

from .registry import ToolRegistry

console = Console()
registry = ToolRegistry()


@click.group()
@click.version_option()
def main():
    """Cursor Tools CLI - Access and run cursor tools from the command line."""
    registry.discover_tools()


@main.command()
def list_tools():
    """List all available tools."""
    tools = registry.get_available_tools()
    console.print("\n[bold]Available Tools:[/bold]\n")

    for tool in tools:
        console.print(f"[green]{tool.name}[/green]: {tool.description}")


@main.command()
@click.argument("tool_name")
@click.argument("args", nargs=-1)
def run(tool_name: str, args: Optional[tuple] = None):
    """Run a specific tool with arguments."""
    try:
        tool = registry.get_tool(tool_name)
        kwargs = {}

        if args:
            # Convert args to kwargs (format: key=value)
            for arg in args:
                if "=" in arg:
                    key, value = arg.split("=", 1)
                    kwargs[key] = value

        result = asyncio.run(tool.execute(**kwargs))
        console.print(f"\n[bold green]Result:[/bold green] {result}\n")

    except KeyError:
        console.print(f"[bold red]Error:[/bold red] Tool '{tool_name}' not found")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")


if __name__ == "__main__":
    main()
