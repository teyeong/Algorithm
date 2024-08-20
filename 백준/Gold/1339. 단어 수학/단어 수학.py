import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    arr.append(input().rstrip())

# 알파벳 저장 딕셔너리
alpha = {}

# 자릿수대로 가중치
for i in range(N):
    for j in range(len(arr[i])):
        if arr[i][j] in alpha:
            alpha[arr[i][j]] += 10 ** (len(arr[i]) - 1 - j)
        else:
            alpha[arr[i][j]] = 10 ** (len(arr[i]) - 1 - j)

# 크기순 정렬
alpha = sorted(alpha.items(), key=lambda x: -x[1])

num = [str(i) for i in range(10)]

for i in range(len(alpha)):
    for j in range(N):
        arr[j] = arr[j].replace(alpha[i][0], num[-1])
    num.pop()

print(sum(int(i) for i in arr))