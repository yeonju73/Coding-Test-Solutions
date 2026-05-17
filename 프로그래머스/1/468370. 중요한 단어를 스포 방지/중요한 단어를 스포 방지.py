def solution(message, spoiler_ranges):
    answer = 0
    
    input_list = list(message.split())
    words_with_indices = list()
    
    # 단어가 시작하는 지점
    start = -1
    
    for i, char in enumerate(message):
        # 단어의 첫 시작이라면
        if char != ' ' and start == -1:
            start = i
        # 띄어쓰기거나 마지막 자리라면
        elif (char == ' ' or i == len(message) - 1) and start != -1:
            
            # end는 띄어쓰기 index
            if char == ' ':
                end = i 
            else:
                end = i + 1
                
            words_with_indices.append((start, end))
            start = -1
        
    is_spoiler = [False] * len(words_with_indices)
    for spo in spoiler_ranges:
        for i in range(len(words_with_indices)):
            
            # 해당 단어가 스포방지 구간에 포함되는지 확인
            start, end = words_with_indices[i]
            
            if not(end <= spo[0] or spo[1] < start):
                is_spoiler[i] = True
    
    print(words_with_indices)
    print(is_spoiler)
    # 스포방지된 단어 중, 스포방지구간이 아닌 영역에서 공개된 적이 있다면 중요한 단어가 아님
    for s in range(len(words_with_indices)):
        # 스포방지 단어일때
        if is_spoiler[s]:
            spo_flag = True
            spo_start, spo_end = words_with_indices[s]
            spo_word = message[spo_start:spo_end]
            
            # 단어중에 스포방지가 안되어 있는 단어 중 같은 단어가 없다면 중요한 단어
            for wr in range(len(words_with_indices)):
                if wr != s and is_spoiler[wr] == False:
                    word_start, word_end = words_with_indices[wr]
                    word = message[word_start:word_end]
                    if word == spo_word:
                        spo_flag = False
                        break
                    
            if spo_flag: answer += 1
            
            # 스포방지 해제
            is_spoiler[s] = False
    
    return answer