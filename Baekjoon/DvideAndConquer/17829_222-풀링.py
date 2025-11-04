import sys
input = sys.stdin.readline

n = int(input().rstrip())
input_matrix = list()
for i in range(n):
    input_matrix.append(list(map(int, input().rstrip().split())))

while n > 1:
    new_size = n // 2
    new_matrix = [[0] * new_size for _ in range(new_size)]
    
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            # 2x2 matrix
            square = [
                input_matrix[i][j],
                input_matrix[i+1][j],
                input_matrix[i][j+1],
                input_matrix[i+1][j+1]
            ]
            # 2번째로 큰 값을 새 행렬에 저장
            square.sort(reverse=True)
            new_matrix[i//2][j//2] = square[1] # new_matrix 의 크기가 절반이 되었으니까
            
    # 다음 반복을 위해 행렬과 크기 업데이트
    input_matrix = new_matrix
    n = new_size
            
# 모든 풀링이 끝나면 matrix는 1x1 행렬 [[결과값]] 이 됨
print(input_matrix[0][0])
