import sys
input = sys.stdin.readline

# 사전순으로 가장 앞서는 답을 출력 -> AAAA -> BB
# 덮을 수 없으면 -1을 출력
input_list = list(input().rstrip().split("."))

def polinomio(input_list):
    result = list()
    
    for i in input_list:
        # 길이가 2로 나누어지지 않으면 바로 종료
        if len(i) % 2 != 0:
            return -1
        
        # len(i)가 0일 경우, result에는 빈 문자열이 삽입됨
        a_part = (len(i)//4) * 'AAAA'
        b_part = ((len(i)%4)//2) * 'BB'
        result.append(a_part + b_part)
        
    return '.'.join(result)

print(polinomio(input_list))