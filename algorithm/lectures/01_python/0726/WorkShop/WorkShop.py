# def duplicated_letters(word):
#     # 최종 반환 리스트
#     result = []
#     # 전체 단어 순회
#     # char -> a, p, p, l, e
#     for char in word:
#         # 만약에
#         # apple이라는 단어에  a라는 알파벳이
#         # 2개 이상 있다면
#         # 중복되어 나온 단어를 모아둘 result에
#         # 해당 알파벳 추가하기
#         if word.count(char) >= 2:
#             # 2개이상 등장하는 알파벳이
#             # result 리스트에 아직 없으면
#             if char not in result:
#                 result.append(char)
#     return result

# print(duplicated_letters('apple')) # => [‘p’]
# print(duplicated_letters('banana')) # => [’a’, ‘n’]


# def low_and_up(word):
#     result = ''

#     for idx, char in enumerate(word):
#         if idx % 2 == 1:
#             result += char.upper()
#         else:
#             result += char.lower()
#     return result


# print(low_and_up('apple')) # => aPpLe
# print(low_and_up('banana')) # => bAnAnA


def lonely(numbers):
    result = []
    for num in numbers:
        if not result:
            result.append(num)
        else:
            if result[-1] != num:
                result.append(num)
    return result

def lonely(numbers):
    result = [numbers[0]] # result = [1]
    # for num in range(1, len(numbers)+1):
    for num in numbers:
        if result[-1] != num:
            result.append(num)
    return result


print(lonely([1, 1, 3, 3, 0, 1, 1])) # => [1, 3, 0, 1]
print(lonely([4, 4, 4, 3, 3])) # => [4, 3]