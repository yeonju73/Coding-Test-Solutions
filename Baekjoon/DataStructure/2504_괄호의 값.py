import sys
input = sys.stdin.readline

# 곱셈용 임시 값 + 스택

input_list = list(input().rstrip())
result = 0
temp = 1

# 괄호 잘 맞나 평가
stack = list()

for i in range(len(input_list)):
    if input_list[i] == '(':
        stack.append('(')
        temp *= 2
        
    elif input_list[i] == '[':
        stack.append('[')
        temp *= 3
        
    elif input_list[i] == ')':
        # 스택이 비어있거나 짝이 안 맞으면
        if not stack or stack[-1] != '(':
            result = 0
            break
        # 바로 앞이 열린 괄호일 때만 result에 값을 더함
        if input_list[i-1] == '(':
            result += temp
        stack.pop()
        temp //= 2
        
    elif input_list[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if input_list[i-1] == '[':
            result += temp
        stack.pop()
        temp //= 3

# stack 에 값이 남아 있으면 괄호가 올바르지X
if stack:
    result = 0 

print(result)