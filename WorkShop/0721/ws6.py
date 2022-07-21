def get_secret_number(word):
    Word=list(word)
    sum=0
    for i in Word:
        sum = sum + ord(i)
    return sum

get_secret_number('haapy')