import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo_keywords = set(input().rstrip() for _ in range(N))
used_keywords = set()
answer = []

cnt = len(memo_keywords)

for _ in range(M):
    new_keywords = list(input().rstrip().split(','))
    
    for w in new_keywords:
        if w in memo_keywords and w not in used_keywords:
            cnt -= 1
    used_keywords.update(new_keywords)
    
    answer.append(cnt)
    

print('\n'.join(map(str, answer)))