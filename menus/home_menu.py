from menus.profile_menu import name_selection
from menus.selection_menu import selection_menu

def home_menu(name, languages):
    print("=================\n"
    "  Language Lab   \n"
    f"  Welcome {name} \n"
    "=================\n")
    for number, language in languages.items(): 
        print(f"{number}. {language['name']}")
