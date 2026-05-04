from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def print_section(title: str, data: dict):
    table = Table(title=title)

    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")

    for key, value in data.items():
        table.add_row(str(key), str(value))

    console.print(table)


def print_result(results):
    for result in results:
        if isinstance(result, Exception):
            console.print(f"[red]Error:[/red] {result}")
            continue

        for key, value in result.items():
            if isinstance(value, dict):
                print_section(key.upper(), value)
            else:
                console.print(Panel(str(value), title=key.upper()))

def calculate_risk(results):
    score = 0

    for result in results:
        if isinstance(result, dict):
            if "hibp" in result:
                score += 50
            if "http_headers" in result:
                score += 10

    return score
