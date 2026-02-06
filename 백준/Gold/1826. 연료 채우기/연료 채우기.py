import heapq

N = int(input())
oilstations = [tuple(map(int, input().split())) for _ in range(N)]
L, P = map(int, input().split())

oilstations.sort()

ans = 0

candidate = []

for a, b in oilstations:
    while P < a:
        if len(candidate) == 0:
            print(-1)
            exit()
        fuel = heapq.heappop(candidate)
        P -= fuel
        ans += 1
    
    heapq.heappush(candidate, -b)

while P < L:
    if len(candidate) == 0:
        ans = -1
        break
    fuel = heapq.heappop(candidate)
    P -= fuel
    ans += 1

print(ans)