import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format

def printLogo():
    cprint(figlet_format("Gymtastic", font="big"), "green")
    cprint("by Christian Dario Nievas, Agustin Ricardo Luna, Emiliano Martin Salvano", "green")
