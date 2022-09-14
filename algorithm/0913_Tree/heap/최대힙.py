def enq(n):
    global last
    last +=1
    heap[last] = n
    #부모가 있고 ,부모 < 자식 인경우 자리 교환
    c = last
    p = c//2 #완전이진트리에서 부모 정점 번호
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c= p #부모를 새로운 자식으로
        p = c//2

def deq():
    global last
    tmp = heap[1]       #루트 백업
    heap[1] = heap[last]# 삭제할 노드의 키를 루트에 복사
    last -= 1           # 마지막 노드 삭제
    p = 1               # 루트에 옮긴 값을 자식과 비교
    c = p * 2           # 왼쪽 자식
    while c <= last:  # 자식이 하나라도있으면
        #오른쪽 자식도 있고, 오른쪽 자식이 더크면
        if c+1 <= last and heap[c] < heap[c+1]:
            c += 1      #비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]: #자식이 더 크면 최대힙어긋남
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:               #부모가 더 크면
            break
    return tmp

heap = [0] * 100
last = 0


print(heap)