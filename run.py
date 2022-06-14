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
# def playing():
#     word = pick_word(my_words):
#     guess_letters =set(word)
#     used_letters = set()