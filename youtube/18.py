score = {
'python': 80,
'django': 89,
'web': 83
}

score['alforithm'] = 90
score.update({'python':85})
print(sum(score.values())//len(score))


