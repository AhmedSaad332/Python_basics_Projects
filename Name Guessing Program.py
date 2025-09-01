import random

names = ["ahmed", "sara", "ali", "yousef", "mona"]

word = random.choice(names).lower()
word_display = ["_"] * len(word)
used_letters = []
max_attempts = 5
remaining_attempts = max_attempts

print("Welcome to the Name Guessing Game!")
print("You have 5 chances to guess the name.")
print("Word:", " ".join(word_display))

while True:
    if "_" not in word_display:
        print(f"\nCongratulations! You guessed the name '{word}' with {remaining_attempts} attempts left!")
        break

    if remaining_attempts == 0:
        print("\nGame Over! The correct name was:", word)
        break

    guess = input("\nEnter a character: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in used_letters:
        print("You already tried this letter.")
        continue

    used_letters.append(guess)
    remaining_attempts -= 1

    if guess in word:
        for i, char in enumerate(word):
            if char == guess:
                word_display[i] = guess
        print("Correct!")
    else:
        print("Wrong guess!")

    print("Word:", " ".join(word_display))
    wrong_guesses = [ch for ch in used_letters if ch not in word]
    print("Wrong guesses:", ", ".join(wrong_guesses) if wrong_guesses else "None")
    print(f"Remaining attempts: {remaining_attempts}")
