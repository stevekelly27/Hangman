import random



def pick_word():
    """
    generates a word from my_words.txt
    """
    my_words = open("requirements.txt", "r")
    words = my_words.readlines()
    my_words.close()

    return random.choice(words)[:-1]

pick_word()


def playing():
    word = pick_word()
    word_letters = set(word)
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    used_letters = set()
    lives = 10 

    while len(word_letters) > 0 and lives > 0:

        print('You have used the letters: ', ' '.join(used_letters))
        print('You have', lives, 'lives left: ')

        current_word = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(current_word))

        guess_letter = input('Guess a letter: ')
        if guess_letter in alphabet:
            used_letters.add(guess_letter)
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)
            else:
                lives = lives -1
                print('ooops, try again!')    

        elif guess_letter in used_letters:
            print('Character already in use. Please try again!') 

        else:
            print('Invalid character. Please try again!')     
    
    if lives == 0:
        print('You died! The correct word was', word, '!')
    else:
        print('Correct! Well done, the word was', word, '!')    
                  

playing()        