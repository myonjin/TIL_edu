def itoa(num):
    # 음수 판별
    negative = False
    if num < 0:
        negative = True
        num = -num

    if num == 0:
        return '0'

    # 넘겨받은 정수를 0이 되기 전까지 계속 반복
    result = ''
    while num:
        # 일의자리 수부터 끊어서 문자열로 변환
        remainder = num % 10
        # atoi -> ord(char) - ord('0')
        result = chr(ord('0') + remainder) + result
        num = num // 10

    # 만약 처음 넘겨 받은 값이 음수였다면
    if negative:
        # 문자열 앞에 '-' 를 붙여서 반환한다.
        return '-' + result
    else:
        return result

print(itoa(123)*3)
print(itoa(0))
print(itoa(-3))