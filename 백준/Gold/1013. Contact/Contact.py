import sys
input = sys.stdin.readline
import re

p = re.compile('^(100+1+|01)+$')
T = int(input())

for _ in range(T):
    s = input().rstrip()
    
    m = p.match(s)
    print("YES" if m else "NO")