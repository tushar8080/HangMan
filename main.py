import random
from hangman_art import logo, stages

from hangman_words import word_list
chosen_word = random.choice(word_list)
# print(f"psst, chosen word is {chosen_word}")
display = []
word_length = len(chosen_word)
lives = 6


print(logo)

for _ in range(word_length):
    display += '_'

end_of_game = False
while not end_of_game:
    guess = input("guess a letter that can be in the word :").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("you loose")

    print(display)

    if "_" not in display:
        end_of_game = True
        print("you win")

    print(stages[lives])
