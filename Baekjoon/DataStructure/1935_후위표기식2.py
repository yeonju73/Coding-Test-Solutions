import sys
input = sys.stdin.readline

n = int(input().strip())
ex = input().strip()
num_list = []

input_list = []
stack = []

for _ in range(n):
    num_list.append(int(input().strip()))
    
for i in ex:
    if 'A' <= i <= 'Z':
       input_list.append(num_list[ord(i) - ord('A')])
    else:
        input_list.append(i)
        
while input_list:
    a = input_list.pop(0)
    
    if type(a) == int:
        stack.append(a)
    else:
        last = stack.pop()
        first = stack.pop()
        
        if a == '*':
            stack.append(first * last)
        elif a == '+':
            stack.append(first + last)
        elif a == '-':
            stack.append(first - last)
        elif a == '/':
            stack.append(first / last)

print("{:.2f}".format(stack.pop()))