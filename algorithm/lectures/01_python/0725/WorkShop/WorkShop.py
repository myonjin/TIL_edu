def get_dict_avg(scores):
    # 결괏값
    result = 0
    # 넘겨받은 dict의 value들만 있으면 된다.
    # 모든 벨류들을 다 모아놓은 값도 필요하겠다.
    # 총합
    # 전체 길이
    idx = 0
    count = 0
    for score in scores.values():
        idx += 1
        count += score
    result = count / idx
    return result
    
def get_dict_avg(scores):
    return sum(scores.values()) / len(scores.values())

print(get_dict_avg({'python' : 80,'web' : 83,'algorithm' : 90,'django' : 89,})) # => 85.5



def count_blood(type):
    result = {}
    for blood in type:
        # 만약에 이미 result에 blood에 해당하는 키값이 있다면
        # if result['result'] # 이 경우, 키가 없으면 오류가 난다.
        if result.get(blood):
            # 그 키값에 1을 추가한다.
            result[blood] += 1
        # 없다면
        else:
            # 그 키와 벨류를 새로 추가한다.
            result[blood] = 1
    return result

def count_blood(type):
    result = {}
    for blood in type:
        result[blood] = result.get(blood, 0) + 1
    return result

print(count_blood(['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']) )














