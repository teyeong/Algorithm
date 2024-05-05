def solution(sequence, k):
    answer = []
    l = len(sequence)
    n = sequence[0]
    index = 0
    
    for i, v in enumerate(sequence):
        while n < k and index <= l - 2:
            index += 1
            n += sequence[index]
        if n == k:
            answer.append([index - i, [i, index]])
        n -= v
    
    answer.sort()
    return answer[0][1]