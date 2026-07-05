from data import languages
from menus import lesson_engine
from lessons.modern_languages.coffee_shop_words import coffee_words
from lessons.modern_languages.restaurant_words import restaurant_words
from lessons.modern_languages.airport_words import airport_words

def selection_menu(profile):
    language_choice = input(
        "\nPlease input the number: "
        "\n"
        )
    while True:
        if language_choice in languages:
                language = languages[language_choice]["code"]
                lesson_choice = input("=================\n"
                "  Language Lab   \n"
                f"  Name: {profile['name']}\n"
                f"Language: {languages[language_choice]['name']} \n"
                "=================\n"
                "\n"
                "  1. Coffee Shop \n"
                "  2. Airport     \n"
                "  3. Restaurant  \n"
                "  4. Change Language       \n"
                "  5. Exit Language Lab  \n"
                )
        if lesson_choice == "1":
            lesson_engine.lesson(profile['name'], language, "Coffee Shop", coffee_words)
        elif lesson_choice == "2":
            lesson_engine.lesson(profile['name'], language, "Airport", airport_words)
        elif lesson_choice == "3":
            lesson_engine.lesson(profile['name'], language, "Restaurant", restaurant_words)
        elif lesson_choice == "4":
             return "change_language"
        elif lesson_choice == "5":
            print("Thank you for choosing Language Lab for your language learning")
            return "exit"
        else:
            print("Invalid selection. Please try again.")
