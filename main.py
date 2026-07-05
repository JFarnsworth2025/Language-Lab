from menus.language_selection_menu import language_selection_menu
from menus.selection_menu import selection_menu
from menus.profile_menu import profile_selection
from data import languages

profile = profile_selection()

if profile == "exit":
    quit()

selecting = True

while selecting:
    
    selected = language_selection_menu(profile, languages)
    result = selection_menu(profile)

    if result == "exit":
        selecting = False