import sys
input = sys.stdin.readline

# 사전순으로 가장 앞서는 답을 출력 -> AAAA -> BB
# 덮을 수 없으면 -1을 출력
input_list = list(input().rstrip().split("."))

def polinomio(input_list):
    result = list()
    
    for i in input_list:
        if i == '':
            result.append('')
        # 길이가 2로 나누어지지 않으면 바로 종료
        elif len(i) % 2 != 0:
            return -1
        elif len(i) % 4 == 0:
            result.append(len(i) * 'A')
        # 4로 나누어 떨어지지 않으면, 최대한 A로 채운 뒤 나머지만 B로 채움
        elif len(i) // 4 > 0:
            result.append(((len(i)//4) * 'AAAA') + ((len(i)%4) * 'B'))
        else:
            result.append(len(i) * 'B')
    return '.'.join(result)

print(polinomio(input_list))