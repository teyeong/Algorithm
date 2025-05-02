def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    length = len(begin)
    visit = [False for _ in range(len(words))]
    idx = 0
    
    while begin != target:
        diff_idx = 0
        cnt = 0 # 새 단어와 begin 간의 차이
        target_cnt = 0 # 타겟과 begin 간의 차이

        if idx > len(words) - 1:
            return 0
        
        if not visit[idx]:
            for i in range(length):
                if begin[i] != words[idx][i]:
                    diff_idx = i
                    cnt += 1
                if target[i] != begin[i]:
                    target_cnt += 1
            
            if target_cnt == 1:
                answer += 1
                begin = target
                break
            if cnt > 1:
                idx += 1
            elif cnt == 1:
                # 타겟이랑 비교
                target_same = 0 # 타겟과 바꾸려는 단어의 일치 알파벳 개수
                begin_same = 0 # 현재와 타겟의 단어의 일치 알파벳 개수
                for i in range(length):
                    if target[i] == words[idx][i]:
                        target_same += 1
                    if begin[i] == target[i]:
                        begin_same += 1
                visit[idx] = True
                if begin_same <= target_same:
                    begin = words[idx]
                    answer += 1
                    idx = 0
                else:
                    idx += 1
        else:
            idx += 1
    
    return answer