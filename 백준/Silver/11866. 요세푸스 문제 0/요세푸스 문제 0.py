N, K = map(int, input().split())

people = [i for i in range(1, N + 1)]
res = []

idx = K - 1

while people:
    res.append(people[idx])
    people.remove(people[idx])
    if people:
        idx = (idx + K - 1) % len(people)

print('<' + ', '.join(map(str, res)) + '>')