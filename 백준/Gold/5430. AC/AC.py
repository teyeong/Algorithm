import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    comm = input()
    n = int(input())
    input_str = input().rstrip().strip('[]')
    if input_str:
        arr = list(map(int, input_str.split(',')))
    else:
        arr = []
    
    flag = 0
    odd = 0
    for ch in comm:
        if ch == "R":
            odd = not odd
        if ch == "D":
            if arr:
                if odd:
                    arr.pop()
                else:
                    arr.pop(0)
            else:
                flag = 1
                break
    if flag:
        print("error")
    else:
        if odd:
            arr.reverse()
        print(str(arr).replace(' ', ''))