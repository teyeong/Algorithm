import sys
input = sys.stdin.readline

N, K = map(int, input().split())

sequence = list(map(int, input().split()))

counter = dict()

curr = 0
max_length = 0

for idx, val in enumerate(sequence):
    if val in counter.keys():
        if counter[val] < K:
            counter[val] += 1
            curr += 1
        else:
            while sequence[idx - curr] != val:
                # 버리기
                counter[sequence[idx - curr]] -= 1
                if counter[sequence[idx - curr]] == 0:
                    del counter[sequence[idx - curr]]
                curr -= 1
    else:
        counter[val] = 1
        curr += 1
    
    max_length = max(max_length, curr)

print(max_length)