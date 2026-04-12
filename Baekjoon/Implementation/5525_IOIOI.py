import sys
input = sys.stdin.readline

n = int(input())
length = int(input())
string_list = list(input().rstrip())

result = 0
cursor = 1
count = 0

while cursor < length - 1:
    if string_list[cursor-1] == 'I' and string_list[cursor] == 'O' and string_list[cursor+1] == 'I':
        # 연속된 패턴 매칭 횟수
        count += 1
        
        # 입력 크기 이상이 됐다면
        if count >= n:
            result += 1
        # 다음 패턴을 볼 수 있는 곳으로 커서 이동
        cursor += 2
        continue
    else:
        count = 0
            
    # 다음 자리로 커서 이동
    cursor += 1
            
print(result)