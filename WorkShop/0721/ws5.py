

def get_secret_word(word):
    a=''
    for i in word:
        a+=chr(i)
    return a

get_secret_word([83,115,65,102,89])