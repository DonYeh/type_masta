import requests
import random


def word_bank():
    word_list = []
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)

    WORDS = response.text.split()  # a list of words

    for word in WORDS:
        word_list.append(word)

    # converted_word = bytes(random.choice(word_list), 'utf-8')
    word_to_spell = random.choice(word_list)

    return word_to_spell
    # return converted_word
    # random.choice(word_list) #picks a random item from the list


# print(word_bank())
