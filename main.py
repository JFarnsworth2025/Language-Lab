from menus.home_menu import home_menu
from menus.selection_menu import selection_menu
from menus.profile_menu import name_selection
from data import languages

name = name_selection()
selecting = True

while selecting:
    
    home_menu(name, languages)
    result = selection_menu(name)

    if result == "exit":
        selecting = False