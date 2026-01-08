N = int(input())
exp = input().rstrip()

numbers = []
operators = []

for e in exp:
    if e == "+" or e == "-" or e == "*":
        operators.append(e)
    else:
        numbers.append(int(e))

limit = 2 ** 31
length = len(numbers) # dp 범위
dp_max = [[-limit for _ in range(length)] for _ in range(length)]
dp_min = [[limit for _ in range(length)] for _ in range(length)]

# dp_max[i][j]: i~j번째 숫자들 연산의 max값
# dp_min[i][j]: i~j번째 숫자들 연산의 min값

for i in range(length):
    dp_max[i][i] = numbers[i]
    dp_min[i][i] = numbers[i]

# 연산할 숫자 수를 기준으로 for loop
for dp_len in range(1, length + 1):
    for i in range(length):
        j = i + dp_len - 1
        if j >= length:
            break
        for k in range(i, j):
            if operators[k] == '+':
                dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
            elif operators[k] == '-':
                dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])
            elif operators[k] == '*':
                dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] * dp_max[k + 1][j], dp_max[i][k] * dp_min[k + 1][j], dp_min[i][k] * dp_max[k + 1][j], dp_min[i][k] * dp_min[k + 1][j])
                dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] * dp_min[k + 1][j], dp_max[i][k] * dp_min[k + 1][j], dp_min[i][k] * dp_max[k + 1][j], dp_max[i][k] * dp_max[k + 1][j])

print(max(dp_max[0][length - 1], dp_min[0][length - 1]))