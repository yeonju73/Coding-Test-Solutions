import sys
input = sys.stdin.readline
output = sys.stdout

# 전위 순회 (루트) (왼쪽 자식) (오른쪽 자식)
def preorder_traversal():
    stack = []
    stack.append('A')
    while stack:
        node = stack.pop()
        if node != '.':
            output.write(node)
            stack.append(graph.get(node)[1])
            stack.append(graph.get(node)[0])

    output.write("\n")
    
# 중위 순회 (왼쪽 자식) (루트) (오른쪽 자식)
def inorder_traversal():
    stack = []
    visited = []
    stack.append('A')
    while stack:
        node = stack.pop()
        
        if node in visited:
            output.write(node)
            continue
        
        visited.append(node)
        
        if graph.get(node)[1] != '.' :
            stack.append(graph.get(node)[1])
        stack.append(node)
        if graph.get(node)[0] != '.' :
            stack.append(graph.get(node)[0])
        
    output.write("\n") 

# 후위 순회 (왼쪽 자식) (오른쪽 자식) (루트)
def postorder_traversal():
    stack = []
    visited = []
    stack.append('A')
    while stack:
        node = stack.pop()
        
        if node in visited:
            output.write(node)
            continue
        
        visited.append(node)
        
        stack.append(node)
        if graph.get(node)[1] != '.' :
            stack.append(graph.get(node)[1])
        if graph.get(node)[0] != '.' :
            stack.append(graph.get(node)[0])
        
    output.write("\n") 

n = int(input().strip())
graph = {chr(ord("A") + i) :[] for i in range(n)}
stack = []
for _ in range(n):
    input_list = input().strip().split()
    graph[input_list[0]].append(input_list[1])
    graph[input_list[0]].append(input_list[2])

preorder_traversal()
inorder_traversal()
postorder_traversal()

output.flush()
output.close()
