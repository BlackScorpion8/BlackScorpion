from rich.console import Console
import os
console = Console()


def display_menu(language):
    console.print("\n" + "=" * 43, style="bold cyan")
    print("Select an option / 选择一个选项:")
    cpu_count = os.cpu_count()
    console.print(f'Number of available processors / 可用处理器数量: {cpu_count}')
    if language == "en":
        console.print("1. Scan subdomains CPU", style="bold green")
        console.print("0. Exit", style="bold green")
    elif language == "cn":
        console.print("1. 子域名探测 CPU", style="bold green")
        console.print("0. 退出", style="bold green")
    return input("> ")
