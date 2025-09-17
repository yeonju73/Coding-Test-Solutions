import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
ket_to_value = dict()
value_to_key = dict()

for i in range(1, n+1):
    input_string = input().strip()
    ket_to_value[i] = input_string
    value_to_key[input_string] = i
    
for _ in range(m):
    input_string = input().strip()
    if input_string.isdigit(): # isdigit: 오로지 숫자로만 이루어진 문자열인지 (음수나 소수점도 false로)
        print(ket_to_value.get(int(input_string)))
    else:
        print(value_to_key.get(input_string))
