#ord('a') == chr(65)
def get_secret_word(list):
    result = []
    for i in list:
        result.append(chr(i))
    result = ''.join(result) # ''.join(리스트) 를 사용해서 리스트를 하나의 문자열로 변환해줌..... 다른 방법??? 
    return(result)
get_secret_word([83, 115, 65, 102, 89])