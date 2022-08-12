def itoa(num):
    # 넘겨받은 정수를 0이 되기 전까지 계속 반복
    # 일의자리 수부터 끊어서 문자열로 변환
    # atoi -> ord(char) - ord('0')
    # 만약 처음 넘겨 받은 값이 음수였다면
    # 문자열 앞에 '-'을 붙여서 반환
    negative = False
    if num < 0:
        negative = True
        num = -num
    if num == 0:
        return '0'
    result = ''
    if num == 0:
        return '0'
    while num:
        remainder =num % 10
        result = chr(ord('0') + remainder) +result
        num = num // 10

    if negative == True:
        # 문자열 앞에 '-' 붙여서 반환
        return '-' + result
    else:
        return result

print(itoa(3))
print(itoa(0))
print(itoa(-3))
print(itoa(14))

