def get_secret_number(word):
    Word=list(word)
    sum=0
    for i in Word:
        sum = sum + ord(i)
    return sum

def get_strong_word(*big):
    if get_secret_number(big[0]) > get_secret_number(big[1]):
        print(big[0])
    elif get_secret_number(big[0]) < get_secret_number(big[1]):
        print(big[1])
    else:
        print(big[0],big[1])



get_strong_word('z', 'a') 
get_strong_word('delilah','dixon')
