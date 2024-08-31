import sys
input = sys.stdin.readline

def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

T = int(input())

for _ in range(T):
    arr = list(input().rstrip())
    
    l, r = 0, len(arr) - 1
    
    ans = 0
    
    while l < r:
        if arr[l] != arr[r]:
            if ans == 0:
                ans = 1
            else:
                ans = 2
                break
            
            if arr[l + 1] == arr[r] and arr[r - 1] == arr[l]:
                if is_palindrome(arr[l + 1:r + 1]):
                    arr.pop(l)
                    l -= 1
                else:
                    arr.pop(r)
                    l -= 1
            elif arr[l + 1] == arr[r]:
                arr.pop(l)
                l -= 1
            elif arr[r - 1] == arr[l]:
                arr.pop(r)
                l -= 1
            else:
                ans = 2
                break
        l += 1
        r -= 1
    print(ans)