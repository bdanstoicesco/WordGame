import random
import string

master_list = ['python', 'java', 'kotlin', 'javascript']
word_to_guess = random.choice(master_list)
word_to_print = "-" * len(word_to_guess)
lives = 8
char_found = []
found = False
print("H A N G M A N")
s = input("Type 'play' to play the game, 'exit' to quit:\n")
if s == 'play':
    pass
else:
    quit()


while lives > 0:
    print()
    print(word_to_print)
    c = input('Input a letter:')
    if len(c) != 1:
        print('You should input a single letter')
        continue
    if c not in string.ascii_lowercase :
        print('Please enter a lowercase English letter')
        continue
    if c in char_found:
        print("You've already guessed this letter")
        continue
    char_found.append(c)
    if c in word_to_guess:
        for i in range(len(word_to_guess)):
            if c == word_to_guess[i]:
                word_to_print = word_to_print[:i] + c + word_to_print[i + 1:]
        if '-' not in word_to_print:
            found = True
            break
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
else:
    print('You lost!')

if found:
    print()
    print(word_to_print)
    print('You guessed the word!')
    print('You survived!')
