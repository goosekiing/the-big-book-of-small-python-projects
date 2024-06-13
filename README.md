# Python Projects from "The Big Book of Small Python Projects"

This repository contains my implementations of several projects from [*The Big Book of Small Python Projects*](https://inventwithpython.com/bigbookpython/) by Al Sweigart. This curated collection of simple Python projects allows you to dive right in and create digital art, games, animations, number-crunching tools, and more.

## About the Book
The book by Al Sweigart is a fantastic resource for anyone looking to develop their Python skills through hands-on projects. Al's approach of learn-by-doing is incredibly effective, and his decision to make the book available for free is a huge benefit to many aspiring programmers. I highly recommend checking it out [here](https://inventwithpython.com/bigbookpython/).

## Projects Included
Here are the projects I've completed:

1. Project 01: Beagels
2. Project 02: Birthday Paradox
3. Project 03: Bitmap Message
4. Project 04: Blackjack
5. Project 05: Bouncing DVD Logo
6. Project 06: Caesar Cipher
7. Project 07: Caesar Hacker
8. Project 08: Calendar Maker
9. Project 10: Cho Han
10. Project 12: Collatz Sequence
11. Project 13: Conway's Game of Life
12. Project 14: Countdown
13. Project 15: Deep Cave
14. Project 26: Fibonacci
15. Project 46: Million Dice Roll Statistics Simulation
16. Project 48: Monty Hall Problem
17. Project 52: Numeral System Problems
18. Project 64: Seven Segment Display Module
19. Project 66: Simple Substitution Cipher
20. Project 80: Vigenère Cipher

All projects were implemented using Python version 3.11.4 and are functioning as proposed in the book, with some improvements.

## Directory Structure
The directory structure is as follows:
```
base_dir/project-n-name/main.py
```
Where `n` is the project number in the book and `name` is the name of the project.

## Additional Information
- For projects that require extra libraries, a `requirements.txt` file is included in the project folder.
- Each project includes the following functions:
  ```python
  def clear_terminal() -> None:
      """Clears the terminal."""
      os.system('cls' if os.name == 'nt' else 'clear')

  if __name__ == "__main__":
      try:
          main()
      except KeyboardInterrupt:
          print("\n-------|-----|-------\nExecution Interrupted\n-------|-----|-------\n")
  ```
  These functions help maintain a clean terminal and ensure proper initialization and termination of the project. The main logic is encapsulated in the `main` function, with various global functions called within `main`.

## Purpose
The primary purpose of this repository is to serve as a backup and to showcase these projects. I do not intend to make any further changes, nor am I seeking contributions. These projects are simple and free for anyone to copy and use.

Feel free to explore the projects and use them as you wish!
