import sys
input = sys.stdin.readline


def solve():
    size = 5
    mylist = [list(map(int, input().rstrip().split())) for _ in range(size)]
    bingolist_flat = [num for row in [list(map(int, input().rstrip().split())) for _ in range(size)] for num in row]
    
    # 딕셔너리를 사용해 숫자의 위치를 저장 {숫자: (행, 열)}
    num_to_pos = {mylist[r][c]: (r, c) for r in range(size) for c in range(size)}
    
    # 각 행, 열, 대각선의 -1 개수를 추적
    rows_marked = [0] * size
    cols_marked = [0] * size
    diag1_marked = 0 # 오른쪽 아래 대각선
    diag2_marked = 0 # 왼쪽 아래 대각선
    bingo_count = 0
    
    for i, num in enumerate(bingolist_flat):
        r, c = num_to_pos.get(num)
        
        rows_marked[r] += 1
        if rows_marked[r] == size:
            bingo_count += 1
        
        cols_marked[c] += 1
        if cols_marked[c] == size:
            bingo_count += 1
        
        if r == c:
            diag1_marked += 1
            if diag1_marked == size:
                bingo_count += 1
        
        # (0, 4), (1, 3), (2, 2), (3, 1), (4, 0)
        if r + c == size - 1:
            diag2_marked += 1
            if diag2_marked == size:
                bingo_count += 1
        
        if bingo_count >= 3:
            print(i + 1)
            break

solve()