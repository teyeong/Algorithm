def solution(n, words):
    turn = [1] * (n + 1)

    idx = 1
    word = words[0]
    last = word[len(word) - 1]

    for i in range(1, len(words)):
        word = words[i]
        turn[idx] += 1
        idx += 1
        if idx > n:
            idx = 1
        if word[0] == last and word not in words[:i]:
            last = word[len(word) - 1]
        else:
            return [idx, turn[idx]]
        
    return [0, 0]