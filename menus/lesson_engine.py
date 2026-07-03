def lesson(name, language, lesson_name, lesson_words):
    print(
        "=================\n"
        "  Language Lab   \n"
        f"  Name: {name}\n"
        f"Lesson: {lesson_name} \n"
        "=================\n"
        "\n")
    for number, words in enumerate(lesson_words, start=1):
        correct_word = words[language]
        print(
            "=====================\n"
            f"Lesson: {lesson_name}\n"
            f"Word: {number} / {len(lesson_words)}\n"
            "=====================\n"
            f"{correct_word}"
        )
        answer = ""
        while answer.lower() != correct_word.lower():
            answer = input("Please type the exact word: ")
            if answer.lower() != correct_word.lower():
                print("Incorrect! Please try again:")
        print("Correct! Your next word:")