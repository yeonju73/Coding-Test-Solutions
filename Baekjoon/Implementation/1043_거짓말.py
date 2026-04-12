import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 상위 부모 찾기
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    # 부모 통일
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().rstrip().split())
peple_list = list(map(int, input().rstrip().split()))[1:]
party_list = list()

# 스스로의 값으로 초기화
parent = list(range(n+1))
print(parent)
result = 0

for _ in range(m):
    new_list = list(map(int, input().rstrip().split()))
    party_list.append(new_list[1:])

    for i in range(1, len(new_list)-1):
        union(new_list[i], new_list[i+1])

# 진실을 아는 사람의 부모 집합
know_set = set()
for know in peple_list:
    know_set.add(find(know))

for party in party_list:
    flag = True
    for p in party:
        if find(p) in know_set:
            flag = False
            break
    if flag: result+=1
    
print(result)