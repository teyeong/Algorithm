import sys
input = sys.stdin.readline

strA = input().rstrip()
strB = input().rstrip()

lcs = [[0 for _ in range(len(strB) + 1)] for _ in range(len(strA) + 1)]

for i in range(1, len(strA) + 1):
    for j in range(1, len(strB) + 1):
        if strA[i - 1] == strB[j - 1]:
            lcs[i][j] = lcs[i - 1][j - 1] + 1
        else:
            lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

print(lcs[len(strA)][len(strB)])