import sys
input = sys.stdin.readline

count = 0
result = -1

# A[p..r]을 오름차순 정렬한다.
def merge_sort(A: list, start, end):
    if start >= end:
        return False
    mid = int((start + end) / 2)
    if merge_sort(A, start, mid):
        return True
    if merge_sort(A, mid+1, end):
        return True
    return merge(A, start, mid, end)

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
def merge(A: list, start, mid, end):
    global count
    global result
    
    i, j, t = start, mid + 1, 0
    tmp = [0] * (end - start + 1)
    
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
        
    while i <= mid:
        tmp[t] = A[i]
        t += 1
        i += 1
    
    while j <= end:
        tmp[t] = A[j]
        t += 1
        j += 1
    
    i = start
    t = 0
    while i <= end:
        A[i] = tmp[t]
        count += 1
        if count == K:
            result = A[i]
            return True
        
        i += 1
        t += 1
        
    return False

N, K = map(int, input().rstrip().split())

input_list = list(map(int, input().rstrip().split()))

merge_sort(input_list, 0, N-1)
print(result)