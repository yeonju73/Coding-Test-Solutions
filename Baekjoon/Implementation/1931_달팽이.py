import sys
input = sys.stdin.readline

def solve():
    n = int(input().rstrip())
    m = int(input().rstrip())

    result = [[0] * n for _ in range(n)]    
    
    # 값 채우는 순서
    # n = 3: 중앙값 (1, 1) 상1 우1 하2 좌2 상2
    # n = 5: 중앙값 (2, 2) 상1 우3 하4 좌4 상4
    # n = 7: 중앙값 (3, 3) 상1 우5 하6 좌6 상6
    
    # 방향(상 하 좌 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    direction_list = []
    
    for i in range(3, n + 1, 2):
        direction_list.append((dx[0], dy[0]))
        for _ in range(i - 2):
            direction_list.append((dx[3], dy[3]))
        for _ in range(i - 1):
            direction_list.append((dx[1], dy[1]))
        for _ in range(i - 1):
            direction_list.append((dx[2], dy[2]))
        for _ in range(i - 1):
            direction_list.append((dx[0], dy[0]))
            
    x = n//2
    y = n//2
    number = 1
    result[x][y] = number
    m_adrr = (x, y)
    
    while(len(direction_list) != 0):
        number += 1
        
        direc = direction_list.pop(0)
        x += direc[0]
        y += direc[1]
        
        if m == number:
            m_adrr = (x, y)
            
        result[x][y] = number
    
    for row in result:
        for r in row:
            print(r, end=" ")
        print()

    print(f"{m_adrr[0] + 1} {m_adrr[1] + 1}")
        
solve()