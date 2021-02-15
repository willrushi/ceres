from colorama import Fore, Style

def green(str):
    return f"{Fore.GREEN}{str}{Style.RESET_ALL}"

def yellow(str):
    return f"{Fore.YELLOW}{str}{Style.RESET_ALL}"

def red(str):
    return f"{Fore.RED}{str}{Style.RESET_ALL}"