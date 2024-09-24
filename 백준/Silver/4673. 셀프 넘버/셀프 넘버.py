arr = [i for i in range(1, 10001)]

for i in range(1, 10001):
    digit_sum = sum(map(int, str(i))) + i
    if digit_sum in arr:
        arr[digit_sum - 1] = 0

for i in arr:
    if i:
        print(i)