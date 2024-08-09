N = int(input())

result = []

for _ in range(N):
    result.append(list(map(int, input().split())))

result.sort(reverse=True, key=lambda x: x[2])

if result[0][0] == result[1][0]:
    country = result[0][0]
else:
    country = -1

print(result[0][0], result[0][1])
print(result[1][0], result[1][1])

for i in range(2, N):
    if country != result[i][0]:
        print(result[i][0], result[i][1])
        break