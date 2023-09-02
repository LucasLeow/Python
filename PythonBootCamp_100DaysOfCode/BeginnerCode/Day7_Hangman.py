import random
import Day7_HangmanArt as hangArt
import Day7_HangmanWords

chosen_word = random.choice(Day7_HangmanWords.countries).lower()
display = ["_" for i in chosen_word]
entered_before = []
mistakes = 6
play_again = True


print("Welcome to Country Guess Hangman")
print(hangArt.logo)
print("Guess the following Country: ")
print(' '.join(display))

while (play_again):
    while ("_" in display):

        if mistakes < 0:
            break

        user_guess = input("Guess a letter: ").lower()
        if len(user_guess) > 1:
            print("Please enter only 1 letter!")
            continue

        if (user_guess in entered_before):
            print("You have already guessed this letter!")
            continue

        entered_before.append(user_guess)

        if (user_guess in chosen_word):
            for i in range(len(chosen_word)):
                if (user_guess == chosen_word[i]):
                    display[i] = user_guess
            print(' '.join(display))
        else:
            print(hangArt.stages[mistakes])
            print(' '.join(display))
            mistakes -= 1

    if mistakes < 0:
        print(f"You lose! The answer was {chosen_word}")
    else:
        print("You win!")
