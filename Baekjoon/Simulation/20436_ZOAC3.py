import sys
input = sys.stdin.readline

sl, sr = input().rstrip().split()
input_list = list(input().rstrip())

keyboard = dict()

left_list = [['q', 'w', 'e', 'r', 't'], 
                 ['a', 's', 'd', 'f', 'g'],
                 ['z', 'x', 'c', 'v']]
right_list = [['y', 'u', 'i', 'o', 'p'], 
                 ['h', 'j', 'k', 'l'],
                 ['b', 'n', 'm']]

line_length = [10, 9, 7]
diff = [5, 5, 4]

for line in range(3):
    for n in range(diff[line]):
        keyboard[left_list[line][n]] = (line, n)
    for n in range(line_length[line] - diff[line]) :
        keyboard[right_list[line][n]] = (line, n + diff[line])

current_left = keyboard[sl]
current_rignt = keyboard[sr]
time = 0

rignt_list_flat = [i for line in right_list for i in line]

for key in input_list:
    trans_time = 0
    
    if key in rignt_list_flat:
        x = abs(current_rignt[0] - keyboard[key][0])
        y = abs(current_rignt[1] - keyboard[key][1])
        trans_time = x + y
        current_rignt = keyboard[key]
        
    else:
        x = abs(current_left[0] - keyboard[key][0])
        y = abs(current_left[1] - keyboard[key][1])
        trans_time = x + y
        current_left = keyboard[key]
    
    time = time + trans_time + 1

print(time)