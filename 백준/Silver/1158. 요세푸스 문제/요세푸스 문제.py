N, K = map(int, input().split())
circle = [i for i in range(1, N + 1)]
result = []
idx = K - 1

while circle:
    if idx >= len(circle):
        idx %= len(circle)
    temp = circle.pop(idx)
    result.append(temp)
    idx += K - 1

answer = "<" + ", ".join(map(str, result)) + ">"
print(answer)