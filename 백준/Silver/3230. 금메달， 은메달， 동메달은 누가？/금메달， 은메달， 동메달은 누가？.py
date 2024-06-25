N, M = map(int, input().split())
race1 = []
race2 = []

for j in range(N):
    rank = int(input())
    race1.insert(rank - 1, j + 1)

player2 = race1[:M] # 두 번째 경주에 참여하는 선수 목록
for _ in range(M):
    rank = int(input())
    player = player2.pop()
    race2.insert(rank - 1, player)

for k in range(3):
    print(race2[k])