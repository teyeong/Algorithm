formula = input().split('-')

num = []

for ch in formula:
    temp_sum = 0
    temp_list = map(int, ch.split('+'))
    
    for i in temp_list:
        temp_sum += i
    num.append(temp_sum)

res = num[0]

for i in range(1, len(num)):
    res -= num[i]
print(res)