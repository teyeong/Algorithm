import sys
input = sys.stdin.readline

N, M = map(int, input().split())
voca = {}

for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if not word in voca:
            voca[word] = 1
        else:
            voca[word] += 1
    

voca = sorted(voca.items(), key=lambda x: (- x[1], -len(x[0]), x[0]))
for t in voca:
    print(t[0])