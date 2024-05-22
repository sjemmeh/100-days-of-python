#Step 4

import random
import hangman_words
import hangman_art

end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
z
lives = 6
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lost! The word was {chosen_word}.")
        else:
            print(f"You have {lives} guesses left.")
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print(f"You win! The word was indeed {chosen_word}!")

    print(hangman_art.stages[lives])