N, M = map(int, input().split())

truth_people = set(input().split()[1:])

cnt = 0

parties = []
parent = list(range(N + 1))

# 파티 입력
for _ in range(M):
    parties.append(set(input().split()[1:]))
    
for _ in range(M):
    for party in parties:
        if party & truth_people:
            truth_people.update(party)

for party in parties:
    if party & truth_people:
        continue
    cnt += 1

print(cnt)