def solution(N, number):
    answer = 0
    
    dp = [[]]
    
    for i in range(1, 9):
        curr_set = set()
        curr_set.add(int(str(N) * i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    curr_set.add(a + b)
                    curr_set.add(a - b)
                    curr_set.add(a * b)
                    if b != 0:
                        curr_set.add(a // b)
        dp.append(curr_set)
        if number in dp[i]:
            return i
    
    return -1