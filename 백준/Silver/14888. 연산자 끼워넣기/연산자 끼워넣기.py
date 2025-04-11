N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split())) # +, -, *, /

global max_result
global min_result

def dfs(num, next_idx):
    global max_result
    global min_result

    if next_idx >= len(numbers):
        max_result = max(max_result, num)
        min_result = min(min_result, num)
        return
    
    for i in range(4):
        if operators[i] > 0:
            if i == 0:
                nnum = num + numbers[next_idx]
            elif i == 1:
                nnum = num - numbers[next_idx]
            elif i == 2:
                nnum = num * numbers[next_idx]
            elif i == 3:
                if num > 0:
                    nnum = num // numbers[next_idx]
                else:
                    nnum = -1 * ((-1 * num) // numbers[next_idx])
            operators[i] -= 1
            dfs(nnum, next_idx + 1)
            operators[i] += 1

max_result = float("-inf")
min_result = float("inf")

dfs(numbers[0], 1)
print(max_result)
print(min_result)