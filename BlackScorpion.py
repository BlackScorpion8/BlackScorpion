from Menu.menu import display_menu
from Module.Scanner_module import Scanner_module
from Module.Scandir_module import Scandir_module
from rich.console import Console
console = Console()


def choose_language():
    logo = r"""
     __        __                      __                                                                __                     
    |  \      |  \                    |  \                                                              |  \                    
    | $$____  | $$  ______    _______ | $$   __         _______   _______   ______    ______    ______   \$$  ______   _______  
    | $$    \ | $$ |      \  /       \| $$  /  \       /       \ /       \ /      \  /      \  /      \ |  \ /      \ |       \ 
    | $$$$$$$\| $$  \$$$$$$\|  $$$$$$$| $$_/  $$      |  $$$$$$$|  $$$$$$$|  $$$$$$\|  $$$$$$\|  $$$$$$\| $$|  $$$$$$\| $$$$$$$\
    | $$  | $$| $$ /      $$| $$      | $$   $$        \$$    \ | $$      | $$  | $$| $$   \$$| $$  | $$| $$| $$  | $$| $$  | $$
    | $$__/ $$| $$|  $$$$$$$| $$_____ | $$$$$$\        _\$$$$$$\| $$_____ | $$__/ $$| $$      | $$__/ $$| $$| $$__/ $$| $$  | $$
    | $$    $$| $$ \$$    $$ \$$     \| $$  \$$\      |       $$ \$$     \ \$$    $$| $$      | $$    $$| $$ \$$    $$| $$  | $$
     \$$$$$$$  \$$  \$$$$$$$  \$$$$$$$ \$$   \$$       \$$$$$$$   \$$$$$$$  \$$$$$$  \$$      | $$$$$$$  \$$  \$$$$$$  \$$   \$$
                                                                                              | $$                              
                                                                                              | $$                              
                                                                                               \$$                              
        """
    console.print(logo, style="bold yellow")
    console.print("\nChoose language / 选择语言:", style="bold cyan")
    console.print("en - English", style="bold red")
    console.print("cn - 中文", style="bold red")

    return input("> ")


def main():
    language = None
    while language not in ["en", "cn"]:
        language = choose_language()

    console.print("\n=== Black Scorpion Toolbox / 黑蝎工具箱 ===", style="bold green")
    while True:
        choice = display_menu(language)
        switch = {
            "1": Scanner_module,
            "2": Scandir_module,
            "0": lambda: exit(0)
        }
        if choice in switch:
            switch[choice](language)
        else:
            console.print("Invalid choice, please try again. / 无效选择，请重试。", style="bold red")




if __name__ == "__main__":
    main()
