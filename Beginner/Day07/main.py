import  random
stages = [
    '''
     +---+
     |   |
     0   |
    /|\\  |
    /\\   |
         |
    ========
    ''',
    '''
     +---+
     |   |
     0   |
    /|\\  |
    /    |
         |
    ========
    ''',
    '''
     +---+
     |   |
     0   |
    /|\\  |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
     0   |
    /|   |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
     0   |
     |   |
         |
         |
    ========
    ''',
    '''
     +---+
     |   |
         |
         |
         |
         |
    ========
    '''
]

lives = 5
word_list = ["aardvark" , "baboon" , "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
place_holder = ""
worrd_length = len(chosen_word)
for possition in range(worrd_length):
    place_holder += "-"
game_over = False
correct_letters =[]
while not game_over:

    guess = input("guess the letter: ").lower()
    display = ''

    for letter in chosen_word:
        if letter == guess:
            display +=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display +="_"
    print(display)
    if guess not in chosen_word:
        lives -=1
        if lives == 0 :
            game_over = True
            print("You lose")


    if "_" not in display:
        game_over = True
        print("You win")
    print(stages[lives])
