import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    
    num_list = []
    for _ in range(n):
        num_list.append(input().rstrip())
    num_list.sort()

    flag = 0
    for i in range(n - 1):
        length = len(num_list[i])
        if num_list[i] == num_list[i + 1][:len(num_list[i])]:
                flag = 1
                break
    
    if flag:
        print("NO")
    else:
        print("YES")