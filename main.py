import subprocess
import os
import colorama
from colorama import Fore, Style
colorama.init()

def custom_ls(args):
    """Custom ls function that lists files in the given directory."""
    path = "."  # Default path
    if args:  # If arguments are provided
        path = args[0] #Take the first argument as the path.

    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")

def change_dir(args):
    """Changes the working directory."""
    if args:
        path = args[0]
        try:
            os.chdir(path) #os.chdir is the correct function.
        except FileNotFoundError:
            print(f"cd: {path}: No such file or directory")
        except NotADirectoryError:
            print(f"cd: {path}: Not a directory")
        except PermissionError:
            print(f"cd: {path}: Permission denied")
        except Exception as e:
            print(f"cd: An unexpected error occurred: {e}")
    else:
        print("cd: missing argument")

def speak_up(args):
    color_dic = {
        "blue": Fore.BLUE,
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN,
        "magenta": Fore.MAGENTA,
        "white": Fore.WHITE,
        "black": Fore.BLACK,
    }
    text = args[0]
    if len(args) > 1:  # Check if color argument is provided.
        color = args[1].lower()  # Convert to lowercase for case-insensitivity.
        if color in color_dic:
            print(f"{color_dic[color]}{text}{Style.RESET_ALL}")
        else:
            print(f"{text}")  # Print without color if color is invalid.
    else:
        print(f"{text}")  # Print without color if no color argument is provided.


def pwd():
    return os.getcwd()

command_directory = {
    "ls": custom_ls,
    "cd": change_dir,
    "speak": speak_up
}

no_arg_commands = {"pwd"}


while True:
    user = os.getlogin()
    cwd=os.getcwd()
    command_input = input(f"{Fore.RED}{user}@{Fore.WHITE}DawnShell>{Fore.LIGHTYELLOW_EX}{cwd}{Style.RESET_ALL}:")
    parts = command_input.split() #split the command into parts.
    command = parts[0] #first part is the command.
    args = parts[1:] #remaining parts are the arguments.

    if command.lower() in ["exit", "quit"]:
        break
    try:
        if command in command_directory:
            command_directory[command](args) #pass the arguments.
        elif command in no_arg_commands:
                print(command_directory[command]())
        else:
            print("No Idea! What do you want, mate?")
    except Exception as e:
        print(f"Error: {e}")