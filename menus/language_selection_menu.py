from menus.profile_menu import profile_selection
from menus.selection_menu import selection_menu

def language_selection_menu(profile, languages):
    print("=================\n"
    "  Language Lab   \n"
    f"  Welcome {profile['name']} \n"
    "=================\n")
    for number, language in languages.items(): 
        print(f"{number}. {language['name']}")