import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
# 학생들은 접속 순서대로 3번부터 N + 2번까지 입장 번호를 받게 된다
# 한 학생에게 출석 코드를 보내게 되면,
# 해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보냄.
# K: 졸고 있는 학생 수 - 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.
# Q: 무작위로 한 명의 학생에게 출석 코드를 보내는 행위를 Q번 반복
# 특정 구간의 입장 번호를 받은 학생들 중에서 출석이 되지 않은 학생들의 수를 구하고 싶다.
N, K, Q, M = map(int, input().rstrip().split())

sleep_student = list(map(int, input().rstrip().split()))
code_student = list(map(int, input().rstrip().split()))

range_list = list()
for _ in range(M):
    range_list.append(tuple(map(int, input().rstrip().split())))

visited = set()

while code_student:
    s = code_student.pop()
    # 졸지 않는 학생일때
    if s not in sleep_student:
        if s not in visited:
            visited.add(s)
        
        # 최대로 돌 수 있는 크기
        iter = (N+2) // s
        for i in range(2, iter+1):
            # 아직 방문한 적이 없고 곧 방문할 리스트에도 없다면 추가
            next = s * i
            if next not in visited and next not in code_student:
                code_student.append(next)

visited = sorted(visited)

for s, e in range_list:
    left_index = bisect_left(visited, s)
    right_index = bisect_right(visited, e)
    count = right_index - left_index
    print(e - s + 1 - count)
