N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort() # 오름차순 정렬

if K >= N:
    print(0)
    exit()

# 간격 저장
btw = []
for i in range(N - 1):
    btw.append(sensor[i + 1] - sensor[i])
btw.sort()

# 가장 큰 간격부터 끊기 -> K - 1개
length = sum(btw[:-(K - 1)]) if K > 1 else sum(btw)

print(length)