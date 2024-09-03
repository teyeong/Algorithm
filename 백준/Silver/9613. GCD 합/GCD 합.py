import sys
input = sys.stdin.readline
import math

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))[1:]
    ans = 0
    
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            ans += math.gcd(nums[i], nums[j])
    print(ans)