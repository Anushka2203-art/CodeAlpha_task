import random

word=["table","power","gravity","banana","horse","cycle","mouse","sparrow","rainbow","fish"]
scr_word=(random.choice(word))

correct_guesses=[]
incorrect_guesses=[]
max_guesses=6

print("----------HANGMAN GAME!!----------")
print("Guess the correct word by guessing a letter")
while len (incorrect_guesses) < max_guesses:
    print("\n" + "="*20)
    display_str=""

    for letter in scr_word:
        if letter in correct_guesses:
            display_str += letter +" "

        else:
            display_str +=" _ "

    print(f"Guess a word: {display_str.strip()}")
    print(f"Wrong Guesses: {incorrect_guesses}")
    print(f"Remaining Attempts: {max_guesses - len(incorrect_guesses)}")

    if "_" not in display_str: 
        print(f"\nYOU WIN!! \nThe word was {scr_word}")
        break

    guess = input("Guess a letter: ").lower().strip()

    if len(guess)!= 1 or not guess.isalpha():
        print("Please guess only one letter at a time!")
        continue

    if guess in correct_guesses or guess in incorrect_guesses:
        print("You already guess this letter!")
        continue

    if guess in scr_word:
        print(f"Correct! {guess} is correct letter in the word")
        correct_guesses.append(guess)

    else:
        print(f"Incorrect! {guess} is incorrect letter in the word")
        incorrect_guesses.append(guess)

else:
    print("\n" + "="*20)
    print(f"GAME OVER!! You lost the guesses.\nThe word was {scr_word}")
