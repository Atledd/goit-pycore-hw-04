from colorama import Fore, Style

def visualize_directory(directory, spacing=0):                                        #Рекурсивне відображення директорії
    try:
        for path in directory.iterdir():
            if path.is_dir():
                print(f"{' ' * spacing}{Fore.BLUE}{path.name}{Style.RESET_ALL}")      # Директорії відображено синім
                visualize_directory(path, spacing + 2)                                # Рекурсивно відобразити піддиректорії
            else:
                print(f"{' ' * spacing}{Fore.GREEN}{path.name}{Style.RESET_ALL}")     # Файли відображено зеленим
    except PermissionError:
        print(f"{' ' * spacing}{Fore.RED}Доступ заборонено: {path.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"Error occured: {e}")