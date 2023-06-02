from rich.console import Console
from rich.prompt import Prompt
import os
import time

console = Console()
prompt = Prompt()

console.print("LeetCode Commit v.1.0", style="bold green", justify="center")
console.print("Author: [bold red]@noobscience[/bold red]", justify="center")

def get_file_count():
    count = 0
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                count += 1
    return count

def get_line_count():
    count = 0
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    for line in f:
                        if line.strip():
                            count += 1
    return count

console.print("Few cool stats of your code:", style="bold")
console.print(f"Total files: [bold blue]{get_file_count()}[/bold blue]")
console.print(f"Total lines: [bold blue]{get_line_count()}[/bold blue]")

commit_choice = prompt.ask("Do you want to commit your code? [y/n]", choices=["y", "n"])
if commit_choice == "y":
    commit_message = prompt.ask("Enter your commit message", default="Add solution")
    os.system(f"git add .")
    os.system(f"git commit -m \"{commit_message}\"")
    confirm = prompt.ask("Do you want to push your code? [y/n]", choices=["y", "n"])
    if confirm == "y":
        with console.status("[bold blue]Preparing[/bold blue]", spinner="aesthetic") as status:
            time.sleep(1)
        os.system(f"git push")
        console.print("Code pushed successfully!", style="bold green")
    else:
        console.print("Code not pushed!", style="bold red")
        with console.status("[bold red]Exiting...[/bold red]", spinner="aesthetic") as status:
            time.sleep(1)
    console.print("Code committed successfully!", style="bold green")
else:
    console.print("Code not pushed!", style="bold red")
    with console.status("[bold red]Exiting...[/bold red]", spinner="aesthetic") as status:
        time.sleep(1)
