import sys
import copy
sys.stdin = open('../1210_사다리/input.txt')
def miro(i,j , arr): # i=99 j=end
    global  result,cnt,result_cnt
    cnt+=1
    if i==0:
        result=j  #x 좌표
        result_cnt=cnt # 이동한 칸개수
        return 1
    else:
        if j-1<0:
            if arr[i][j+1]==1:
                arr[i][j] = 0
                miro(i, j + 1,arr)
            else:
                miro(i-1,j,arr)
        elif j+1>99:
            if arr[i][j-1]==1:
                arr[i][j] = 0
                miro(i, j - 1,arr)
            else:
                miro(i-1,j,arr)

        elif 0<=j-1 and arr[i][j-1]==1: #왼쪽
            arr[i][j]=0
            miro(i,j-1,arr)
        elif j+1<=100 and arr[i][j+1]==1: #오른쪽
            arr[i][j]=0
            miro(i,j+1,arr)
        else:
            miro(i-1,j,arr)



for _ in range(1,11):
    tc=int(input())
    maze=[list(map(int,input().split())) for _ in range(100)]
    result = 0   # 도착할때 j의 값
    arr = []     # 도착에서 출발하는 j의 좌표 값들
    result_cnt=0
    for aa in range(100):
        if maze[99][aa] == 1:
            arr.append(aa)
    max_result=0
    min_result_cnt=9999

    for cc in arr:
        cnt=-1
        maze_a = copy.deepcopy(maze)
        miro(99, cc , maze_a) #result , result_cnt (x좌표) (카운트수)
        if result_cnt<min_result_cnt:
            min_result_cnt=result_cnt
            max_result=result
        if result_cnt==min_result_cnt:
            if max_result<result:
                max_result=result

    print(f'#{tc} {max_result}')


