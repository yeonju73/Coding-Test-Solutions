import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
peple_list = list(map(int, input().rstrip().split()))
know_set = set()

result = m

# 한 명이라도 있을 때
if len(peple_list) > 1:
    for peo in peple_list[1:]:
        know_set.add(peo)

for i in range(m):
    new_list = list(map(int, input().rstrip().split()))
    new_set = set(new_list[1:])
    
    # 파티에 온 사람이랑 알고있는 사람이랑 겹치는 사람이 있을 경우
    # -> 진실을 얘기한다
    if len(new_set.intersection(know_set)) > 0:
        know_set.add(new_set)
    # 없을 경우 과장된 얘기를 한다.
    
print(result)