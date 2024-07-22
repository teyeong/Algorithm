N = int(input())

if N < 10:
    print(N)
    exit(0)

digit = 1
i = 2
j = 1
prev = max_num = 9

# 자릿수 구하기
while True:
    max_num += 9 * (10 ** j) * i
    
    if prev < N and max_num >= N:
        break
    
    i += 1
    j += 1
    prev = max_num

cnt = (N - (prev + 1)) // i         # 구한 자릿수에서 몇 번째 숫자
num = str((10 ** (i - 1)) + cnt)    # 해당하는 숫자
idx = (N - (prev + 1)) % i          # 해당하는 인덱스

print(num[idx])