# def count_vowels(word):
#     # 모음 개수 반환
#     result = 0
#     # 일단 전체 순회는 당연한 일
#     # .count() 사용 하기로 했는데... 어떻게 작동 하는지 부터 알아야
#     # for char in word:
#     #     if char in 'aeiou':
#     #         result += 1
#     for char in 'aeiou':
#         result += word.count(char)

#     return result

# print(count_vowels('alpha')) # => 2
# print(count_vowels('banana')) # => 3
# print(count_vowels('aeiou')) # => 5


def only_square_area(widths, heights):
    # 결괏값
    result = []
    #  정사각형?
    # 모든 가로길이. 모든 세로길이 중에
    # 가로와 세로의 길이가 같은 경우에만
    # 두 값을 곱해서 result에 append
    for width in widths:
        for height in heights:
            if width == height:
                result.append(width*height)

    return result

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))