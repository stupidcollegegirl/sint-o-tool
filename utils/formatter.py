from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import print as rprint

console = Console()

def print_result(result):

    if isinstance(result, list):
        for item in result:
            if isinstance(item, dict):
                print_result(item)
        return

    if isinstance(result, str):
        console.print(f"[yellow]Result: {result}[/yellow]")
        return

    if not isinstance(result, dict):
        console.print(f"[red]error: {type(result)}[/red]")
        return

    for key, value in result.items():
        if key.endswith("_error"):
            console.print(f"[red][!] {key.replace('_', ' ').title()}: {value}[/red]")
            continue


        console.print(Panel(f"[bold cyan]{key.upper()}[/bold cyan]", expand=False))

        if isinstance(value, dict):
            table = Table(show_header=True, header_style="bold magenta", title="")
            table.add_column("field", style="dim")
            table.add_column("value")

            for k, v in value.items():
                if v is None or str(v).strip() == "":
                    continue

                if isinstance(v, str) and v.startswith("http"):
                    table.add_row(str(k).replace("_", " ").title(), f"[green]{v}[/green]")
                else:
                    table.add_row(str(k).replace("_", " ").title(), str(v))

            console.print(table)

        elif isinstance(value, bool):
            console.print(f"[bold]Found:[/bold] {'[green]Yes[/green]' if value else '[red]No[/red]'}")
        else:
            rprint(f"[bold]{key}[/bold]: {value}")


def calculate_risk(result) -> int:

    if not isinstance(result, dict):
        return 0

    score = 0


    if "username" in result and isinstance(result["username"], dict):
        found_count = sum(1 for v in result["username"].values() if v and isinstance(v, str) and v.startswith("http"))
        score += found_count * 25


    if "phone" in result and isinstance(result["phone"], dict):
        if result["phone"].get("valid"):
            score += 35


    if "ip_geo" in result:
        score += 30

       if "hibp" in result:
        hibp_data = result["hibp"]
        if isinstance(hibp_data, dict) and hibp_data.get("count", 0) > 0:
            score += 50

    return min(score, 100)
