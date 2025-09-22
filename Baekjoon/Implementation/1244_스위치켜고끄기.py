import sys
input = sys.stdin.readline
output = sys.stdout

switchNum = int(input().rstrip())
switchList = list(map(int, input().rstrip().split()))
studentNum = int(input().rstrip())
studentTupleList = list()

for _ in range(studentNum):
    studentTupleList.append(tuple(map(int, input().rstrip().split())))
    
for student in studentTupleList:
    # 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
    changeSwitch = student[1]
    if student[0] == 1:
        count = 1
        while((count * changeSwitch) <= switchNum):
            switchList[count * changeSwitch - 1] = (switchList[count * changeSwitch - 1] * (-1)) + 1
            count += 1
            
    # 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다. 
    else:
        switchList[changeSwitch - 1] = switchList[changeSwitch - 1] * -1 + 1
        count = 1
        while(((changeSwitch + count) <= switchNum) and (0 < (changeSwitch - count) <= switchNum)):
            left = changeSwitch + count - 1
            right = changeSwitch - count - 1
            if switchList[left] == switchList[right]:
                switchList[left] = switchList[left] * -1 + 1
                switchList[right] = switchList[right] * -1 + 1
                count += 1
            else:
                break
    
for i in range(len(switchList)):
    if i != 0 and i % 20 == 0:
        output.write("\n")
    output.write(f"{switchList[i]} ")
output.write("\n")

output.flush()
output.close()