import sys
input = sys.stdin.readline

N, S = map(int, input().split())

numbers = list(map(int, input().split()))

cnt = 0

def subset_sum(idx, sub_num):
    global cnt
    
    if idx >= N:
        return
    
    sub_num += numbers[idx]
    
    if sub_num == S:
        cnt += 1
    
    subset_sum(idx + 1, sub_num)
    subset_sum(idx + 1, sub_num - numbers[idx])

subset_sum(0, 0)
print(cnt)