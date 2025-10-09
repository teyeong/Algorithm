import sys
input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))

raindrop = 0
curr = 0

for idx in range(1, W - 1):
    left = max(height[:idx])
    right = max(height[idx + 1:])
    curr = min(left, right) - height[idx]
    if curr > 0:
        raindrop += curr
        
print(raindrop)