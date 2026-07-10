This repository contains my first intership's two beginner-friendly Python projects a:Basic Chatbot and a classic Hangman Game.These projects demonstrate core programming principles like conditional logic, loops, error handling, and string manipulation.

# Overview:-

  🤖 Basic Chatbot:
 The Basic Chatbot is a simple text-based conversational partner that runs continuously in a terminal loop. It parses user input for specific keywords and triggers dynamic, predefined responses, mimicking a simple interactive helper.

  🔤 Hangman Game:
The Hangman Game is a word-guessing terminal game. The program selects a random word from a preset list, and the player must guess it one letter at a time within a limited number of incorrect attempts (6). The UI updates dynamically to show correctly guessed letters as blanks (_) or characters.


# Features:-
   
  🤖 Chatbot Features:
  1. Continuous Loop Execution: Stays open and runs continuously until the user types bye or exit.
  2. Case-Insensitive Parsing: Standardizes user text by automatically converting it to lowercase and stripping excess whitespaces.
  3. Keyword Matching: Detects multiple variations of conversational triggers (e.g., greetings, asking for the name, time, weather, or a joke).
  4. Fallback Exception Handler: Safely responds with a polite default message if the input keyword isn't recognized.
  
  🔤 Hangman Game Features:
  1. Random Word Generation: Pulls a hidden word dynamically from a predefined list during every new run.
  2. Input Validation: Restricts input to only individual alphabetic letters; alerts users if they type numbers, multiple characters, or symbols.
  3. Duplicate Guess Tracking: Prevents players from losing turns by identifying if a letter has already been tried.
  4. Visual Board Updates: Live statistics display correct character positions, list of accumulated wrong guesses, and the remaining attempt count.
  
  
  # Used Technologies:-

  1. Language: Python 3.x
  2. Built-in Modules: 'random' (Used for picking random elements from lists in the Hangman game)
  
  
# What I Learnt in This Project? 
   
Building these projects helped solidify fundamental concepts of Python development:-

  1. Flow Control & Loops: Mastered while loops for handling game state tracking and continuous program runtime alongside conditional statements (if-elif-else) for logic-branching.
  
  2. String Manipulation & Methods: Implemented string standardizations such as .lower(), .strip(), .isalpha(), and string concatenations to sanitize input and manage presentation layout.
  
  3. Data Structures: Utilized Python lists ([]) to dynamic append (.append()) tracked data arrays, storing guess histories systematically.
  
  4. User Experience (UX) Guardrails: Learned how to structure input validations to filter out bad values gracefully without crashing the running software.
  
  
# 🚀 How to Run:-
 1. Clone this repository.
 2. Navigate to the project folder.
 3. Run the scripts using Python.
