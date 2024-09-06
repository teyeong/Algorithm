import sys
input = sys.stdin.readline

N = int(input())
liquid = sorted(list(map(int, input().split())))

start, end = 0, N - 1
mid = (start + end) // 2
min_sum = sys.maxsize

for start in range(N - 2):
    mid, end = start + 1, N - 1
    while mid < end:
        temp = liquid[start] + liquid[mid] + liquid[end]

        if abs(min_sum) >= abs(temp):
            res = [liquid[start], liquid[mid], liquid[end]]
            min_sum = temp
    
        if temp < 0:
            mid += 1
        else:
            end -= 1

print(' '.join(map(str, res)))