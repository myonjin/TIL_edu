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
    tmp = heap[1] #루트 백업
    heap[1] = heap[last]# 삭제할 노드의 키를 루트에 복사
    last -= 1  # 마지막 노드 삭제

heap = [0] * 100
last = 0

enq(2)
enq(5)