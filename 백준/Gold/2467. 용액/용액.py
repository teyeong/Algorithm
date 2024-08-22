import sys
input = sys.stdin.readline

N = int(input())

liquid = list(map(int, input().split()))

liquid.sort()

start, end = 0, len(liquid) - 1
min_sum = 1e10
l = r = 0

while start < end:
    if min_sum > abs(liquid[start] + liquid[end]):
        min_sum = abs(liquid[start] + liquid[end])
        l = start
        r = end
    if abs(liquid[start]) < abs(liquid[end]):
        end -= 1
    else:
        start += 1
print(liquid[l], liquid[r])