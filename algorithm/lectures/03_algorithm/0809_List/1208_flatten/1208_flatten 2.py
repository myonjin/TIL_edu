import sys
sys.stdin = open('input.txt')

def search():
    # 인자로 넘겨도 되나 return 과정 코드 가독성 저하
    # max_v, min_v, max_idx, min_idx = search(max_v, min_v, max_idx, min_idx)
    global max_v, min_v, max_idx, min_idx
    for i in range(100):
        if boxes[i] > max_v:
            max_v, max_idx = boxes[i], i
        if boxes[i] < min_v:
            min_v, min_idx = boxes[i], i

for tc in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # 최소, 최대 값 위치
    min_idx = max_idx = 0
    # 박스는 최소 1
    max_v = 0
    # 박스는 최대 100
    min_v = 101
    # 덤프 가능한 동안 반복
    while dump > 0:
        # 최소, 최대 값과 위치 찾기
        search()

        # 찾아온 최소 최대 값 위치 1 감소
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        # 비교 대상 초기화
        max_v = 0
        min_v = 101
        # 덤프 횟수 -1
        dump -= 1
    # 덤프 종료 후 최소, 최대 값 다시 찾기
    search()
    print(f'#{tc} {max_v-min_v}')



