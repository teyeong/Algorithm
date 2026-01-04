from collections import Counter

S = list(input())

counter = Counter(S)

len_0 = counter['0'] // 2
len_1 = counter['1'] // 2

# 앞에서부터 1을 지움
# 뒤에서부터 0을 지움

cnt_0 = 0
cnt_1 = 0
start = 0
end = len(S) - 1

while (cnt_0 < len_0 or cnt_1 < len_1) and start < len(S) and end > -1:
    if S[start] == '1' and cnt_1 < len_1:
        S[start] = -1
        cnt_1 += 1
    if S[end] == '0' and cnt_0 < len_0:
        S[end] = -1
        cnt_0 += 1
    start += 1
    end -= 1

answer = ''
for s in S:
    if s == -1:
        continue
    answer += s
print(answer)