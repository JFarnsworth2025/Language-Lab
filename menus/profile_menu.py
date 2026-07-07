import json
import uuid
from pathlib import Path
from data import languages

profiles_folder = Path("profiles")

def create_profile():

    name = input("======================\n"
                 "What is your name?: ")
    
    print("===================\n"
              "What is your native language? \n"
              "======================\n")
    
    for number, language in languages.items():
        print(f"{number}. {language['name']}")

    language_choice = input("Please select one: ")

    while language_choice not in languages:
        print("Please enter a valid language")
        language_choice = input("Please select one: ")
    
    native_language = languages[language_choice]["code"]

    profile_id = str(uuid.uuid4())

    profile = {
        "id": profile_id,
        "name": name,
        "native_language": native_language
    }

    save_profile(profile)
    print(f"Profile '{name}' created successfully.")

    return profile

def save_profile(profile):
    profiles_folder.mkdir(exist_ok=True)
    filename = profile["id"] + ".json"
    profile_path = profiles_folder / filename

    with profile_path.open("w", encoding="utf-8") as file:
        json.dump(profile, file, indent=4, ensure_ascii=False)

def profile_selection():

    print(
    "=================\n"
    "   Language Lab  \n"
    "=================")

    choice = input("1. Select Profile\n"
        "2. Create Profile\n"
        "3. Exit Language Lab\n"
        "Selection: ")
    
    if choice == "1":
        return load_profiles()
    elif choice == "2":
        return create_profile()
    elif choice == "3":
        return "exit"

def load_profiles():
    profile_files = list(profiles_folder.glob("*.json"))
    if len(profile_files) == 0:
        print(
             "=================\n"
            "No profiles found.\n"
            "=================\n"
        )
        return create_profile()

    print(
        "=================\n"
        "Available Profiles\n"
        "=================\n"
    )

    for number, profile_path in enumerate(profile_files, start=1):
        with profile_path.open("r", encoding="utf-8") as profile_file:
            profile = json.load(profile_file)

    print(f"{number}. {profile['name']}")
    
    while True:
        profile_choice = input("\nPleaase select a profile: ")

        try:
            profile_choice = int(profile_choice)

        except ValueError:
            print("Please enter a valid number.")
            continue

        if profile_choice < 1 or profile_choice > len(profile_files):
            print("Please choose a valid profile.")
            continue
        break

    selected_profile_path = profile_files[profile_choice - 1]
    
    with selected_profile_path.open('r', encoding="utf-8") as file:
        profile = json.load(file)
    
    return profile