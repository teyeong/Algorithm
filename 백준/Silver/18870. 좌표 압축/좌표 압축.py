N = int(input())
x = list(map(int, input().split()))

comp = list(set(x)) # 중복 요소 제거
comp.sort() # 정렬

def search(num): # 이진 탐색
    start, end = 0, len(comp) - 1
    while start <= end:
        mid = (start + end) // 2
        if comp[mid] < num:
            start = mid + 1
        elif comp[mid] > num:
            end = mid - 1
        else:
            return mid
    return start

for i in range(N):
    print(search(x[i]), end=" ")