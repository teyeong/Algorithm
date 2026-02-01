T, A, B = map(int, input().split())

# fullness[0][f] : 물을 안 마심
# fullness[1][f] : 물을 마심
fullness = [[False for _ in range(T + 1)] for _ in range(2)]

fullness[0][0] = True

# 물을 안 마시고 먹기
for i in range(T + 1):
    if fullness[0][i]:
        if i + A <= T:
            fullness[0][i + A] = True
        if i + B <= T:
            fullness[0][i + B] = True

# 물 마시기
for i in range(T + 1):
    if fullness[0][i]:
        fullness[1][i // 2] = True

# 물 마신 후 다시 먹기
for i in range(T + 1):
    if fullness[1][i]:
        if i + A <= T:
            fullness[1][i + A] = True
        if i + B <= T:
            fullness[1][i + B] = True

for i in range(T, -1, -1):
    if fullness[0][i] or fullness[1][i]:
        print(i)
        break