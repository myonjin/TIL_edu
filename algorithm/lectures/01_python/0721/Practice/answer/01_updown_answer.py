import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    # 1. 숫자 입력 받기
    while True:
        print()

        # 1-1. 입력 문구
        number = int(input('1이상 10000이하의 숫자를 입력하세요. : '))

        # 1-2. 범위 바깥 숫자를 입력 받으면 1-1로 되돌아감
        if number < 1 or number > 10000:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요.')
            continue

        # 2. 정답 맞히기
        counts += 1  # 플레이어의 시도 회수 1 증가

        # 2-1. 플레이어의 숫자와 정답을 비교하여 Up, Down을 출력
        if number < answer:
            print('Up!!!')
        elif number > answer:
            print('Down!!!')
        else:
            # 2-2. 정답이라면 시도 회수와 함께 정답 문구를 출력하고 반복문 탈출
            print(f'Correct!!! {counts}회 만에 정답을 맞히셨습니다.')
            print()
            break

    # 3. 게임 재시작 여부 파악하기
    # 3-1. 재시작 여부 문구
    user_choice = input('게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요. : ')

    # 3-2. y를 입력 받으면 재시작
    if user_choice == 'y':
        print()
        continue  # continue로 인해 아래 종료 로직이 실행되지 않고 게임을 다시 반복

    # 3-3. n을 입력 받으면 종료
    # 3-4. y와 n 이외의 다른 문자를 입력 받으면 종료
    if user_choice == 'n':
        print('이용해주셔서 감사합니다. 게임을 종료합니다.')
    else:
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')

    is_playing = False  # 게임 종료를 위해 False로 변경
