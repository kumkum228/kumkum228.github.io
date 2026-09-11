# 🧠 Interactive Python Quiz Game

## 📖 About The Project
This is a command-line Trivia Quiz Game built entirely using fundamental Python concepts. It was developed as a core project for the Python programming course at Glasgow Clyde College. The game tests players' knowledge across different categories with multiple-choice questions, a scoring system, and interactive features.

## ✨ Features
*   **Categories:** Multiple question categories (e.g., Python Basics, General Knowledge).
*   **Scoring System:** Players earn +10 points for correct answers and lose -5 points for incorrect ones.
*   **50:50 Lifeline:** A special one-time use lifeline that eliminates two incorrect options to help the player.
*   **High Score Leaderboard:** Uses basic File Handling (`scores.txt`) to save and display the top scores of past players.
*   **No External Libraries:** Built strictly using Python's built-in data structures (Lists, Nested Dictionaries) and control flows (Loops, If-Else, Functions).

## 🛠️ Technologies Used
*   **Language:** Python 3.x
*   **Core Concepts:**
    *   Nested Dictionaries (Question Bank)
    *   Lists & Strings
    *   While/For Loops
    *   Functions & Modular Code
    *   File I/O (Read/Write)

## 🚀 How to Run the Game
1. Ensure you have Python installed on your system.
2. Clone or download this project folder.
3. Open your terminal or command prompt.
4. Navigate to the project directory.
5. Run the following command:
   ```bash
   python quiz_game.py
   ```

## 🎮 How to Play
1. From the **Main Menu**, choose `1` to Play, `2` for Rules, `3` for the Leaderboard, or `4` to Exit.
2. Enter your name when the quiz starts so your score can be saved.
3. For each question, type the number of your chosen option (`1`–`4`).
4. Type `L` on any question to use your one-time **50:50 Lifeline** (removes two wrong options).
5. When the quiz ends, your final score is saved automatically and can be viewed on the **Leaderboard**.

## 📂 Project Files
| File | Purpose |
|------|---------|
| `quiz_game.py` | The complete game (menu, questions, scoring, lifeline, leaderboard). |
| `scores.txt` | Auto-created on first play. Stores past scores in `name,score` format. |
| `README.md` | This file. |

> **Note:** `scores.txt` does not exist until you finish your first game — the program creates it automatically.
