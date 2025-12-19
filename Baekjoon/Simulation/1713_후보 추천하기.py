import sys
input = sys.stdin.readline
# 비어있는 사진틀이 없는 경우 추천받은 횟수가 가장 적은 것 삭제
# 두 명 이상이면 오래된 사진 삭제
N = int(input())
vote_count = int(input())
input_list = list(map(int, input().rstrip().split()))

vote_dict = dict()

for i in range (vote_count):
    vote_num = input_list[i]
    
    # 사진틀이 비어있거나 남는 곳이 있고 새로운 후보라면 삽입한다.
    if len(vote_dict) == 0 or (len(vote_dict) < N and vote_num not in vote_dict.keys()):
        vote_dict[vote_num] = [1, i]
        
    # 사진틀에 이미 있는 후보가 또 투표를 받았을 때 추천받은 횟수를 증가시킨다.
    elif vote_num in vote_dict.keys():
        value = vote_dict.get(vote_num)
        value[0] += 1
        vote_dict[vote_num] = value
    
    # 사진틀이 꽉 차 있을 때는 추천 받은 횟수가 가장 적은 사진을 삭제
    # 동일하면 가장 오래된 사진 삭제
    elif len(vote_dict) == N:
        # 추천받은 횟수로 정렬하고, 같을 때 투포 시각순으로 정렬
        sorted_list = sorted(vote_dict.items(), key = lambda x: (x[1][0], x[1][1]))
        
        vote_dict.pop(sorted_list[0][0])
        vote_dict[vote_num] = [1, i]

print(*sorted(vote_dict.keys()))