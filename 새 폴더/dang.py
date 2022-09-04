w_list = [25, 3.2, [5.5, 5.30, 5.23, 5.144, 5.00, 5.73]]


# 칠 공을 선택할 때, 각도와 거리 중 각도를 얼마나 비중있게 할 지를 결정하는 w1
# 세기를 조절하는 w2. 크면 세기가 줄어든다.
# 타겟구에 얼마나 두껍게 맞출 것인지를 정하는 w3 (각각 거리가 멀 때, 각도가 15, 30, 60, 90 이하일 때. 그리고 구의 지름인 5.73)

# 두 좌표 사이의 각도 구하기
def angle_cal(A, B):
    whiteBall_x = A[0]
    whiteBall_y = A[1]

    targetBall_x = B[0]
    targetBall_y = B[1]

    # width, height: X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(height / width) if width > 0 else 0
    angle = 180 / math.pi * radian

    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270

    # 목적구가 흰 공을 중심으로 1사분면에 위치했을 때 각도를 재계산
    if whiteBall_x < targetBall_x and whiteBall_y < targetBall_y:
        angle = 90 - (180 / math.pi * radian)

    # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        angle = 270 + (180 / math.pi * radian)

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        angle = 270 - (180 / math.pi * radian)

    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        angle = 90 + (180 / math.pi * radian)

    return angle


# 두 좌표 사이 거리 계산
def dist_cal(A, B):
    width = abs(B[0] - A[0])
    height = abs(B[1] - A[1])
    distance = math.sqrt(width ** 2 + height ** 2)

    return distance


# target, nontarget, black 구분
if order == 1:
    target_list = [balls[i] for i in [1, 3] if balls[i][0] != -1]
else:
    target_list = [balls[i] for i in [2, 4] if balls[i][0] != -1]
nontarget_list = [balls[i] for i in range(1, 6) if balls[i][0] != -1]
black_ball = balls[5]


# 경로에 방해 구가 있는지 확인
def path_inspect(A, B, C):  # A, B 경로 사이 C리스트 공들이 겹치는지

    a = -math.tan(math.radians(-angle_cal(A, B) - 90))
    b = 1
    c = - A[1] - A[0] * a

    # 경로에 상대 구가 있는지 확인
    cnt = 0
    for k in range(len(C)):
        # AB 직선과 C 안 구의 좌표와의 거리
        d = abs(a * C[k][0] + b * C[k][1] + c) / math.sqrt(a ** 2 + b ** 2)

        if A[0] <= B[0]:  # 구의 경로만 계산하고 경로밖은 겹쳐도 괜찮다.
            if A[1] <= B[1]:  # A공을 중심으로 했을 때 B공의 위치가 1사분면
                if A[0] < C[k][0] < B[0] and A[1] < C[k][1] < B[1]:
                    if d < 5.73:
                        cnt = 1
                        break
            else:  # 4사분면
                if B[0] < C[k][0] < A[0] and B[1] < C[k][1] < A[1]:
                    if d < 5.73:
                        cnt = 1
                        break
        else:
            if A[1] <= B[1]:  # 2사분면
                if A[0] < C[k][0] < B[0] and A[1] < C[k][1] < B[1]:
                    if d < 5.73:
                        cnt = 1
                        break
            else:  # 3사분면
                if A[0] < C[k][0] < B[0] and B[1] < C[k][1] < A[1]:
                    if d < 5.73:
                        cnt = 1
                        break

        if cnt == 1:
            return 0
        else:
            return 1


# white_ball과 target_ball이 주어졌을 때 6개의 구멍에 대한 거리, 각도, 방해구 여부를 확인하여 후보들 반환
def find_cand(white_ball, target_ball):
    cand_list = []
    cnt = 0
    for j in range(6):  # 6개의 구멍으로 넣을 경로를 생각해본다.
        angle_target_to_hole = angle_cal(target_ball, HOLES[j])
        angle_white_to_target = angle_cal(white_ball, target_ball)

        if (abs(angle_white_to_target - angle_target_to_hole) > 75):  # 불가능 하다면 버린다.
            pass
        else:  # 타게팅 위치는 구멍과 타겟볼을 잇는 직선에서 타겟볼 뒷편으로 구의 지름만큼 떨어진 지점이다.
            target_site = [target_ball[0] - w_list[2][-1] * math.sin(math.radians(angle_target_to_hole)),
                           target_ball[1] - w_list[2][-1] * math.cos(math.radians(angle_target_to_hole))]
            if path_inspect(white_ball, target_ball, nontarget_list) and path_inspect(target_ball, HOLES[j],
                                                                                      nontarget_list):
                dist_sum = dist_cal(target_ball, HOLES[j]) + dist_cal(white_ball, target_site)
                cand_list += [[target_ball, HOLES[j], dist_sum, abs(angle_white_to_target - angle_target_to_hole)]]

    return cand_list


# 샷 가능한 경로들 찾기
cand_list = []  # [타겟 위치, 구멍위치, 거리, 두께(각도차)]
L = len(target_list)
if L > 0:  # 내 목적구가 남아 있는 경우
    # 경로 후보들 찾기
    for i in range(L):  # 넣어야 하는 공들에 대해
        cand_list += find_cand(balls[0], target_list[i])
else:  # 검은공만 남은 상태
    cand_list = find_cand(balls[0], black_ball)

# 후보 경로들 비교
if len(cand_list) != 0:
    temp = cand_list[0][2] + cand_list[0][3] * w_list[0]
    idx = 0
    for i in range(len(cand_list)):
        new_temp = cand_list[i][2] + cand_list[i][3] * w_list[0]
        if new_temp < temp:
            temp = new_temp
            idx = i
else:  # 칠 수 있는 경로가 없는 경우
    if L > 0:
        cand_list += [[target_list[0], HOLES[0], 100, 0]]
    else:
        cand_list += [[black_ball, HOLES[0], dist_cal(balls[0], black_ball), 0]]
    idx = 0
    print("칠 수 있는 경로가 없음")
    # 이때는 쿠션을 고려해야 한다. 코드는 아직 미구현하여 아무 타겟구를 치도록 하였다.

# 최적 후보를 치는 각도와 세기
print(balls[0], cand_list)
print(idx)

dist_sum = cand_list[idx][2]

if dist_sum / w_list[1] > 100:
    power = 100
elif dist_sum / w_list[1] < 10:
    power = 10
else:
    power = dist_sum / w_list[1]

if dist_sum > 300:
    w3 = w_list[2][0]
elif cand_list[idx][3] < 15:
    w3 = w_list[2][1]
elif cand_list[idx][3] < 30:
    w3 = w_list[2][2]
elif cand_list[idx][3] < 60:
    w3 = w_list[2][3]
else:
    w3 = w_list[2][4]

target_site = [cand_list[idx][0][0] - w3 * math.sin(math.radians(angle_cal(cand_list[idx][0], cand_list[idx][1]))),
               cand_list[idx][0][1] - w3 * math.cos(math.radians(angle_cal(cand_list[idx][0], cand_list[idx][1])))]
angle = angle_cal(balls[0], target_site)