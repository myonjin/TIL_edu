import sys
sys.stdin = open('input.txt')
from itertools import combinations
        # a=list(combinations(arr,i))

T=int(input())
for tc in range(1,2):
    N=int(input())
    food=[]
    for i in range(1,N+1):
        food.append(i)
    arr=[list(map(int, (input().split()))) for _ in range(N)]
    subset_group1=list(combinations(food,N//2))
    subset_group2=[]
    for i in range(len(subset_group1)):
        a=[]
        for j in food:
            if j not in subset_group1[i]:
                a.append(j)
        subset_group2.append(a)
    print(subset_group1)
    print(subset_group2)
    for i in range(len(subset_group1)):
        subset_group1_synergy = list(combinations(subset_group1[i], 2))
        subset_group2_synergy = list(combinations(subset_group2[i], 2))
        print(subset_group1_synergy)
        print(subset_group2_synergy)
        print('-----------------------------')
        group1=0
        group2=0
        final=[]
        for i in range(len(subset_group1_synergy)):
            group1+=arr[subset_group1_synergy[i][0]-1][subset_group1_synergy[i][1]-1] + arr[subset_group1_synergy[i][0]-1][subset_group1_synergy[i][1]-1]
            print(subset_group1_synergy[i][0]-1)
            print(arr[subset_group1_synergy[i][0]-1][subset_group1_synergy[i][1]-1])
        for i in range(len(subset_group1_synergy)):
            group2 += arr[subset_group2_synergy[i][1] - 1][subset_group2_synergy[i][0] - 1] + arr[subset_group2_synergy[i][1] - 1][subset_group2_synergy[i][0] - 1]
        result=abs(group1-group2)
        final.append(result)
        print(group1,group2)
        answer=min(final)
        print(answer)