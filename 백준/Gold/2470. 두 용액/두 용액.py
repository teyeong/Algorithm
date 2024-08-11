import sys
input = sys.stdin.readline

N = int(input())

val = list(map(int, input().split()))

val.sort()

first = 0
last = N - 1

min_val = sys.maxsize

while first < last:
    cur_val = abs(val[first] + val[last])
    if min_val > cur_val:
        min_val = cur_val
        idx1 = first
        idx2 = last
    if abs(val[first]) > abs(val[last]):
        first += 1
    else:
        last -= 1

print(val[idx1], val[idx2])