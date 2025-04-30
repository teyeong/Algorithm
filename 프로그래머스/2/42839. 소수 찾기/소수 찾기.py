import itertools

def solution(numbers):    
    # prime number
    is_prime = [False, False] + [True] * (10 ** len(numbers))
    num_set = set()
    
    for i in range(2, (10 ** len(numbers))):
        if is_prime[i] == True:
            for j in range(i * 2, (10 ** len(numbers)), i):
                is_prime[j] = False
    
    # 모든 경우의 수 찾기
    answer = 0
    for i in range(len(numbers)):
        perm = itertools.permutations(list(numbers), i + 1)
        for num in list(perm):
            int_num = int(''.join(list(num)))
            if is_prime[int_num] and int_num not in num_set:
                num_set.add(int_num)
                answer += 1
    
    return answer