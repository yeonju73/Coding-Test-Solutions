import sys
input = sys.stdin.readline

N = int(input())
total = int(input())
votes = list(map(int, input().rstrip().split()))

frames = list()  # [학생번호, 추천수, 게시시간]

for time, student in enumerate(votes): # voteindex, value
    # 이미 게시된 경우 추천받은 수를 증가시킨다.
    found = False
    for frame in frames:
        if frame[0] == student:
            frame[1] += 1
            found = True
            break
    if found:
        continue
    
    # 사진틀에 남는 곳이 있고 새로운 후보라면 삽입한다.
    if len(frames) < N:
        frames.append([student, 1, time])
        continue
    
    # 사진틀이 꽉 차 있을 때는 추천 받은 횟수가 가장 적은 사진을 삭제
    # 동일하면 가장 오래된 사진 삭제
    remove_idx = 0
    for i in range(1, N):
        # 학생 번호 비교 후, 같으면 시간을 기준으로 비교
        if ((frames[i][1], frames[i][2]) < (frames[remove_idx][1], frames[remove_idx][2])):
            remove_idx = i
            
    frames.pop(remove_idx)
    frames.append([student, 1, time])
    
result = sorted(frame[0] for frame in frames)
print(*result)