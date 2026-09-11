# 🎤 Presentation Speaking Script — Trivia Quiz Game

**For:** Iian Shaw · Glasgow Clyde College · Python (Beginner)
**Project file:** `quiz_game.py`

> **How to use this:** These are your speaking notes — read them out loud a
> couple of times to practise. Speak slowly, and it's okay to have this sheet
> in front of you. Total time: about 3–4 minutes.

---

## 1. Opening (about 20 seconds)

> "Hello, my project is a **command-line Trivia Quiz Game** written in Python.
> It asks the player multiple-choice questions across two categories, keeps a
> score, and it even has a **50:50 lifeline** and a **high-score leaderboard**
> that saves to a file. I built it using only the basics we've learned —
> loops, if-statements, functions, lists, and dictionaries. No external
> libraries."

*(Take a breath. Now open the file or run it.)*

---

## 2. Show it running (about 40 seconds)

> "Let me quickly run it."

*(Run `py quiz_game.py`. Show the menu.)*

> "This is the **main menu** — the player can Play, read the Rules, view the
> Leaderboard, or Exit. I'll play a quick round."

*(Answer one or two questions. Use the 50:50 on one.)*

> "When I type **L**, the 50:50 lifeline removes two wrong answers — and it can
> only be used once per game. At the end, it asks for my name and saves my
> score to the leaderboard."

---

## 3. Explain the Question Bank (about 45 seconds)

> "The questions are stored in a **nested dictionary** called `QUESTION_BANK`.
> Let me explain what 'nested' means here.
>
> The outer dictionary's **keys** are the category names — 'Python Basics' and
> 'General Knowledge'. Each of those holds a **list** of questions. And each
> question is itself a **small dictionary** with three keys: the question text,
> a list of four options, and the correct answer.
>
> So it's a dictionary, inside a list, inside a dictionary — that's the
> 'nesting'. To read the questions, I use **two loops**: an outer loop for the
> categories and an inner loop for each question inside them."

**If asked why:** "I stored the answer as the actual text, like `"def"`, not as
a number. That makes checking the answer really simple — I just compare the
option the player picked to the correct one."

---

## 4. Explain the 50:50 Lifeline (about 45 seconds)

> "The 50:50 lifeline uses two things working together.
>
> First, a **True/False flag** called `lifeline_available`. It starts as True.
> The moment the player uses the lifeline, I set it to False, so it can never
> be used again in that game.
>
> Second, a **helper function** called `use_fifty_fifty`. It builds a new,
> shorter list that keeps the correct answer plus just **one** wrong option —
> so two wrong answers get removed.
>
> Before allowing the lifeline, the code checks that flag. If it's already been
> used, it politely tells the player they can't use it again."

---

## 5. Explain the File I/O / Leaderboard (about 40 seconds)

> "For the leaderboard, I used **File Input/Output**.
>
> When a game ends, I open a text file called `scores.txt` in **append mode**
> and write the player's name and score on a new line.
>
> When the player views the leaderboard, I **open the same file in read mode**,
> loop through each line, and split it back into a name and a score to display
> them, sorted highest first.
>
> One important detail: the **very first time** someone plays, that file
> doesn't exist yet. So I wrapped the reading in a **try/except** — if the file
> isn't found, it just shows 'No scores yet' instead of crashing."

---

## 6. Closing (about 20 seconds)

> "So in summary, this project brings together loops, functions, nested
> dictionaries, and file handling to make a complete, playable game — while
> only using Python basics. Thank you. I'm happy to answer any questions."

---

## 🛡️ Quick answers if you get stuck

| If Iian asks… | Say… |
|---|---|
| "Why so many functions?" | "To keep it organised — each function does one job, so it's easy to read, fix, and reuse." |
| "What if `scores.txt` doesn't exist?" | "It won't crash — `try/except FileNotFoundError` catches it and shows 'No scores yet'." |
| "How do you stop bad input crashing it?" | "A `while True` loop keeps asking until the input is valid — I check `.isdigit()` and the number range." |
| "What would you add next?" | "A timer per question, or more categories — the structure makes it easy to extend." |

---

### ✅ Before you present — a 20-second checklist
- [ ] Python works: run `py --version` (should show a version number).
- [ ] You're in the right folder (`cd` into your `Quiz_Game` folder).
- [ ] Run the game once beforehand so `scores.txt` already has a score to show.
- [ ] Have this script and the study guide open or printed.

**You've got this. Good luck! 🎓**
