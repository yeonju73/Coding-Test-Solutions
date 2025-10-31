import sys
from collections import deque
input = sys.stdin.readline

input_list = deque(input().rstrip())
stack = list()

while input_list:
    char = input_list.popleft()
        
    # 공백일 경우
    if char == ' ':
        while stack:
            print(stack.pop(), end='')
        print(' ', end='')
        
    # 괄호일 경우
    elif char == '<':
        while stack:
            print(stack.pop(), end='')
            
        print(char, end='')
        while True:
            tag_char = input_list.popleft()
            print(tag_char, end='')
            if tag_char == '>':
                break  
            
    # 그냥 문자일 경우
    else:
        stack.append(char)
            
while stack:
    print(stack.pop(), end='')
