def get_dict_avg(scores):
    count=0
    for score in scores.values():
        count+=score    
    return count/len(scores.values())



print(get_dict_avg({
    'python' : 80,
    'web' : 83,
    'algorithm' : 90,
    'django' : 89,
    }))