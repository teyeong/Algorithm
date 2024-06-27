n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
arr.sort()
arr = [k for k in arr if k < x]
start, end = 0, len(arr) - 1
while start < end:
    temp = arr[start] + arr[end]
    if x == temp:
        cnt += 1
        start += 1
        end -= 1
    elif x < temp:
        end -= 1
    else:
        start += 1
print(cnt)