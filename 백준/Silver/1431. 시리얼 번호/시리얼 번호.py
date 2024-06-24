def sum_str_num(s):
    result = 0
    for i in s:
        if i >= '0' and i <= '9':
            result += int(i)
    return result

N = int(input())
serial = []
for _ in range(N):
    serial.append(input())

serial.sort(key=lambda x: (len(x), (sum_str_num(x), x)))
for j in serial:
    print(j)