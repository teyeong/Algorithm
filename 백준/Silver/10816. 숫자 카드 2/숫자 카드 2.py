import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
arr_dict = {}

for i in range(N):
    if arr1[i] in arr_dict:
        arr_dict[arr1[i]] += 1
    else:
        arr_dict[arr1[i]] = 1

M = int(input())
arr2 = list(map(int, input().split()))

for i in range(M):
    if arr2[i] in arr_dict:
        arr2[i] = arr_dict[arr2[i]]
    else:
        arr2[i] = 0
print(' '.join(map(str, arr2)))