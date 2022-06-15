import random


def pick_word():
    """
    generates a word from my_words.txt
    """
    my_words = open("words.txt", "r")
    words = my_words.readlines()
    my_words.close()

    return random.choice(words)[:-1]


def playing():
    lives = 10
    word = pick_word()
    word_letters = set(word)
    used_letters = set()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    while len(word_letters) > 0 and lives > 0:

        print('You have used the letters: ', ' '.join(used_letters))
        print(f'You have {lives} lives left:')

        current_word = [
            letter if letter in used_letters else '-' for letter in word]
        print('Word: ', ' '.join(current_word))

        guess_letter = input('Guess a letter: ').lower().strip()
        if guess_letter in alphabet:
            used_letters.add(guess_letter)
            if guess_letter in word_letters:
                word_letters.remove(guess_letter)
            else:
                lives = lives - 1
                print('ooops, try again!')

        elif guess_letter in used_letters:
            print('Character already in use. Please try again!')

        else:
            print('Invalid character. Please try again!')

    if lives == 0:
        print(f'You died! The correct word was {word}!')
    else:
        print(f'Correct! Well done, the word was {word}!')


playing()
def main():
    keep_playing = True

    while(keep_playing):
        playing()
        user_keep_playing_response = input(
            '\nDo you want to keep playing? (y/n)').lower().strip()
        keep_playing = (user_keep_playing_response == 'y')


if __name__ == '__main__':
    main()