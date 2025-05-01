def solution(n, lost, reserve):
    clothes = [1 for _ in range(n)]
    
    for idx in reserve:
        clothes[idx - 1] += 1
    for idx in lost:
        clothes[idx - 1] -= 1
    
    for idx, val in enumerate(clothes):
        if val == 0:
            if 0 <= idx - 1:
                if clothes[idx - 1] > 1:
                    clothes[idx - 1] -= 1
                    clothes[idx] += 1
                    continue
            if idx + 1 < n:
                if clothes[idx + 1] > 1:
                    clothes[idx + 1] -= 1
                    clothes[idx] += 1
    
    return n - clothes.count(0)