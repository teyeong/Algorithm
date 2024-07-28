N = int(input())

turn = 1 # 상근 = 0, 창영 = 1

while N != 0:
    if N >= 3:
        N -= 3
    else:
        N -= 1
    turn = (turn + 1) % 2

if turn:
    print("CY")
else:
    print("SK")