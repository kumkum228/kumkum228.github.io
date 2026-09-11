"""
======================================================================
  TRIVIA QUIZ GAME  (Command-Line Edition)
======================================================================
A beginner-friendly, interactive trivia game.

This project intentionally uses ONLY basic Python:
    - while / for loops
    - if / elif / else statements
    - functions (def)
    - lists
    - dictionaries (including nested dictionaries)

It does NOT use: external libraries, classes (OOP), or GUI frameworks.

Features:
    1. A Main Menu (Play, Rules, Exit).
    2. A Question Bank built from nested dictionaries
       (2 categories, 6 questions total, 4 options each).
    3. A scoring system (+10 for a correct answer, -5 for a wrong one).
    4. A "50:50" lifeline that can be used ONCE per whole game to
       remove two of the wrong options.
    5. Clean, readable console output using basic string formatting.

Author: (your name)
Course: Glasgow Clyde College - Python (Beginner)
======================================================================
"""


# ----------------------------------------------------------------------
# THE QUESTION BANK
# ----------------------------------------------------------------------
# This is a "nested dictionary": a dictionary whose values are themselves
# lists of dictionaries.
#
# Structure:
#   QUESTION_BANK  -> dictionary
#     "Python Basics" -> a list of questions (category)
#         each question -> a dictionary with 3 keys:
#             "question" : the text of the question (a string)
#             "options"  : a list of 4 possible answers
#             "answer"   : the correct option, written EXACTLY as it
#                          appears in the "options" list
#
# Storing the correct answer as its text (not a number like "option 2")
# makes the code easier to read and much harder to get wrong.
# ----------------------------------------------------------------------
QUESTION_BANK = {

    "Python Basics": [
        {
            "question": "Which keyword is used to create a function in Python?",
            "options": ["func", "def", "function", "define"],
            "answer": "def"
        },
        {
            "question": "What data type is the value: True ?",
            "options": ["int", "str", "bool", "float"],
            "answer": "bool"
        },
        {
            "question": "Which symbol starts a comment on a single line?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        }
    ],

    "General Knowledge": [
        {
            "question": "What is the capital city of Scotland?",
            "options": ["Glasgow", "Edinburgh", "Aberdeen", "Dundee"],
            "answer": "Edinburgh"
        },
        {
            "question": "How many days are there in a leap year?",
            "options": ["364", "365", "366", "367"],
            "answer": "366"
        },
        {
            "question": "Which planet is known as the 'Red Planet'?",
            "options": ["Venus", "Jupiter", "Mars", "Saturn"],
            "answer": "Mars"
        }
    ]
}


# ----------------------------------------------------------------------
# HELPER FUNCTION: print a tidy divider line
# ----------------------------------------------------------------------
def print_line(character="=", width=60):
    """
    Print a horizontal line to make the console output look clean.

    Parameters:
        character (str): the character to repeat (default "=").
        width (int): how many times to repeat it (default 60).

    A string multiplied by a number repeats it, so "=" * 3 gives "===".
    """
    # Multiply the character by the width to build the line, then print it.
    print(character * width)


# ----------------------------------------------------------------------
# FUNCTION: show the main menu and read the user's choice
# ----------------------------------------------------------------------
def show_main_menu():
    """
    Display the main menu and return the user's chosen option.

    Returns:
        str: "1", "2" or "3" (Play, Rules, or Exit).

    A 'while True' loop keeps asking until the user types a valid choice,
    so the program never crashes on unexpected input.
    """
    # Keep looping until we 'return' a valid choice.
    while True:
        print_line()                                   # top divider
        print("        WELCOME TO THE TRIVIA QUIZ GAME!")
        print_line()
        print("  1. Play Game")                        # menu option 1
        print("  2. Rules")                            # menu option 2
        print("  3. Exit")                             # menu option 3
        print_line()

        # input() always returns a string. .strip() removes any accidental
        # spaces the user typed before or after their choice.
        choice = input("  Enter your choice (1-3): ").strip()

        # Check the choice against the three valid values.
        if choice == "1" or choice == "2" or choice == "3":
            return choice          # 'return' sends the value back and stops the loop
        else:
            # Invalid input: warn the user, then the loop repeats.
            print("\n  >> Invalid choice. Please type 1, 2 or 3.\n")


# ----------------------------------------------------------------------
# FUNCTION: display the game rules
# ----------------------------------------------------------------------
def show_rules():
    """
    Print the rules of the game in a clean, easy-to-read layout.
    This function only prints text; it does not return anything.
    """
    print_line()
    print("                  GAME RULES")
    print_line()
    print("  * Answer each multiple-choice question by typing")
    print("    the option number (1, 2, 3 or 4).")
    print()
    print("  * Scoring:")
    print("        Correct answer  -> +10 points")
    print("        Wrong answer    ->  -5 points")
    print()
    print("  * 50:50 Lifeline:")
    print("        Type 'L' instead of an answer to remove TWO")
    print("        wrong options. You can use this ONCE per game.")
    print_line()

    # Pause so the user can read the rules before returning to the menu.
    input("  Press ENTER to return to the main menu... ")


# ----------------------------------------------------------------------
# FUNCTION: use the 50:50 lifeline
# ----------------------------------------------------------------------
def use_fifty_fifty(options, correct_answer):
    """
    Build a shorter list of options for the 50:50 lifeline.

    The new list keeps the correct answer and ONE wrong answer,
    so two wrong options are removed.

    Parameters:
        options (list): the 4 original options.
        correct_answer (str): the correct option text.

    Returns:
        list: a smaller list containing the correct answer plus one
              wrong answer (2 options in total).
    """
    # Start with a list that already contains the correct answer.
    reduced_options = [correct_answer]

    # Loop through every original option.
    for option in options:
        # We want to add exactly ONE wrong option to keep the total at 2.
        if option != correct_answer and len(reduced_options) < 2:
            reduced_options.append(option)

    # Return the shortened list of options (correct + one wrong).
    return reduced_options


# ----------------------------------------------------------------------
# FUNCTION: ask a single question and return the points earned
# ----------------------------------------------------------------------
def ask_question(question_data, lifeline_available):
    """
    Display one question, handle the user's answer, and score it.

    Parameters:
        question_data (dict): a single question dictionary with the keys
                              "question", "options" and "answer".
        lifeline_available (bool): True if the 50:50 lifeline has not
                                   been used yet.

    Returns:
        A list of two values: [points_earned, lifeline_available]
            points_earned (int): +10, -5, or 0.
            lifeline_available (bool): updated flag (becomes False if the
                                       lifeline was used on this question).

    We return two things in a list so the main game loop knows both the
    score change AND whether the lifeline is still available.
    """
    # Pull the pieces of the question out of the dictionary for easy use.
    question_text = question_data["question"]
    options = question_data["options"]
    correct_answer = question_data["answer"]

    # Print the question text.
    print()
    print("  Q: " + question_text)
    print()

    # Keep asking this same question until we get a valid response.
    while True:
        # enumerate() gives us both a counter and the item.
        # We 'start=1' so the numbering shown is 1, 2, 3, 4 (not 0-based).
        for number, option in enumerate(options, start=1):
            print("     " + str(number) + ". " + option)

        # Build the prompt. If the lifeline is still available, mention it.
        if lifeline_available:
            print()
            prompt = "  Your answer (1-" + str(len(options)) + "), or 'L' for 50:50: "
        else:
            print()
            prompt = "  Your answer (1-" + str(len(options)) + "): "

        # Read the answer. .strip() removes spaces; .upper() lets the user
        # type 'l' or 'L' for the lifeline.
        user_input = input(prompt).strip().upper()

        # ---- CASE 1: the user asks for the 50:50 lifeline ----
        if user_input == "L":
            if lifeline_available:
                # Shrink the options down to 2 (correct + one wrong).
                options = use_fifty_fifty(options, correct_answer)
                # Mark the lifeline as used so it cannot be used again.
                lifeline_available = False
                print("\n  >> 50:50 used! Two wrong options removed.\n")
                # 'continue' jumps back to the top of the while loop so the
                # question is shown again with only 2 options.
                continue
            else:
                # The lifeline was already used earlier in the game.
                print("\n  >> You have already used your 50:50 lifeline!\n")
                continue

        # ---- CASE 2: the user typed an answer number ----
        # .isdigit() checks the text is made only of digits (e.g. "3").
        if user_input.isdigit():
            chosen_number = int(user_input)   # convert the text to a number

            # Check the number is within the valid range of options.
            if 1 <= chosen_number <= len(options):
                # Lists start at index 0, so option 1 is at index 0.
                chosen_option = options[chosen_number - 1]

                # Compare the chosen option text to the correct answer.
                if chosen_option == correct_answer:
                    print("\n  >> Correct! (+10 points)\n")
                    # Return points earned and the (unchanged) lifeline flag.
                    return [10, lifeline_available]
                else:
                    print("\n  >> Wrong! (-5 points)")
                    print("     The correct answer was: " + correct_answer + "\n")
                    return [-5, lifeline_available]

        # ---- CASE 3: anything else is invalid; loop and ask again ----
        print("\n  >> Invalid input. Please try again.\n")


# ----------------------------------------------------------------------
# FUNCTION: play one full game (all questions in all categories)
# ----------------------------------------------------------------------
def play_game():
    """
    Run a complete game: loop through every category and every question,
    keep track of the score, and show a final result at the end.
    """
    score = 0                      # the player's running score
    lifeline_available = True      # the 50:50 can be used once; start as True
    question_number = 1            # a counter to label questions nicely

    print_line()
    print("                  STARTING THE QUIZ!")
    print_line()

    # Outer loop: go through each category in the question bank.
    # .items() gives us both the category name (key) and its questions (value).
    for category_name, questions in QUESTION_BANK.items():

        # Announce the category with a small header.
        print()
        print("  ----- CATEGORY: " + category_name + " -----")

        # Inner loop: go through each question inside this category.
        for question_data in questions:

            # Show a friendly question label, e.g. "Question 1".
            print("\n  Question " + str(question_number) + ":")

            # Ask the question. It returns [points, updated_lifeline_flag].
            result = ask_question(question_data, lifeline_available)

            # Unpack the returned list into two clear variables.
            points_earned = result[0]
            lifeline_available = result[1]

            # Update the score and the question counter.
            score = score + points_earned
            question_number = question_number + 1

            # Show the running score after each question.
            print("  Current score: " + str(score))

    # After both loops finish, the game is over. Show the final summary.
    print()
    print_line()
    print("                  QUIZ COMPLETE!")
    print_line()
    print("  Your final score is: " + str(score) + " points")

    # A simple message based on how well the player did.
    if score >= 50:
        print("  Excellent work! You're a trivia champion!")
    elif score >= 20:
        print("  Nice job! A solid performance.")
    elif score >= 0:
        print("  Good effort - keep practising!")
    else:
        print("  Don't worry - try again to improve your score!")
    print_line()

    # Pause before returning to the main menu.
    input("  Press ENTER to return to the main menu... ")


# ----------------------------------------------------------------------
# FUNCTION: the main program loop
# ----------------------------------------------------------------------
def main():
    """
    The starting point of the program.

    It shows the main menu on repeat until the user chooses to exit.
    This is the function we call at the very bottom of the file to
    actually start the game.
    """
    # Keep the program running until the user picks "Exit".
    while True:
        # Ask the menu function for the user's choice.
        choice = show_main_menu()

        # Decide what to do based on that choice.
        if choice == "1":
            play_game()            # start a full game
        elif choice == "2":
            show_rules()           # display the rules
        elif choice == "3":
            # Say goodbye and 'break' out of the while loop to end the program.
            print("\n  Thanks for playing. Goodbye!\n")
            break


# ----------------------------------------------------------------------
# PROGRAM START
# ----------------------------------------------------------------------
# This standard Python line means: "only run main() if this file is being
# run directly (not imported into another file)." For a beginner project
# you can simply read it as: 'this is where the program begins.'
if __name__ == "__main__":
    main()
