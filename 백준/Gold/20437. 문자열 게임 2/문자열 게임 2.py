from collections import defaultdict
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    W = input().rstrip()
    K = int(input().rstrip())
    
    idxs = defaultdict()
    
    for i, w in enumerate(list(W)):
        if w in idxs.keys():
            idxs[w] += [i]
        else:
            idxs[w] = [i]
    
    max_len = 0
    min_len = len(W)
    
    for alpha, idx in idxs.items():
        if len(idx) < K:
            continue
        
        for i in range(len(idx) - K + 1):
            max_len = max(max_len, idx[i + K - 1] - idx[i] + 1)
            min_len = min(min_len, idx[i + K - 1] - idx[i] + 1)
    
    if max(len(i) for i in idxs.values()) < K:
        print(-1)
    else:
        length = [len(W), len(W)]
        
        if K == 1:
            print(1, 1)
        else:
            print(min_len, max_len)