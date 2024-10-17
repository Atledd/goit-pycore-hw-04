import sys
from colorama import Fore, Style
from pathlib import Path
from functions import visualize_directory

def main():
    try:
        directory = Path(sys.argv[1])
        if not directory.exists():
            raise FileNotFoundError("Such directory does not exist.")
        if not directory.is_dir():
            raise NotADirectoryError("Path does not lead to the directory.")
        
        print(f"{Fore.YELLOW}Your directory: {directory}{Style.RESET_ALL}")
        visualize_directory(directory)

    except FileNotFoundError as fnfe:
        print(Fore.RED + str(fnfe) + Style.RESET_ALL)
    except NotADirectoryError as nade:
        print(Fore.RED + str(nade) + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)

if __name__ == "__main__":
    main()