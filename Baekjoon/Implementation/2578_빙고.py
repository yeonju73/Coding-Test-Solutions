import sys
input = sys.stdin.readline

def check_3_bingo():
    count = 0
    
    # 가로 빙고 체크
    for i in range(size):
        for j in range(size):
            if mylist[i][j] != -1:
                break
            elif j == size-1:
                count += 1
                
    # 세로 빙고 체크
    for i in range(size):
        for j in range(size):
            if mylist[j][i] != -1:
                break
            elif j == size-1:
                count += 1
    
    # 오른쪽 대각선 빙고 체크
    for i in range(size):
        if mylist[i][i] != -1:
            break
        elif i == size-1:
            count += 1
    
    # 왼쪽 대각선 빙고 체크
    for i in range(size):
        if mylist[size-i-1][i] != -1:
            break
        elif i == size-1:
            count += 1
            
    return count >= 3

size = 5
mylist = list()
bingolist = list()

for _ in range(size):
    mylist.append(list(map(int, input().rstrip().split())))

for _ in range(size):
    bingolist.append(list(map(int, input().rstrip().split())))

for lineCount in range(size):
    for c in range(size):
        for row in range(size):
            for col in range(size):
                if mylist[row][col] == bingolist[lineCount][c]:
                    mylist[row][col] = -1
                    if check_3_bingo():
                        print((lineCount * size) + (c + 1))
                        exit(0)
                    break