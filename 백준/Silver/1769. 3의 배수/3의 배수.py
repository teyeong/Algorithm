X = input()
list_x = list(X)

cnt = 0
while len(list_x) != 1:
    res = str(sum(map(int, list_x)))
    list_x = list(res)
    cnt += 1

print(cnt)
if int(list_x[0]) % 3 == 0:
    print("YES")
else:
    print("NO")