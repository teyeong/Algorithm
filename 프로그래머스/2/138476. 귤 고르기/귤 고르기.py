def solution(k, tangerine):
    tangerine.sort()
    cnt = [0] * (tangerine[-1] + 1)
    for i in range(len(tangerine)):
        cnt[tangerine[i]] += 1
    box = 0
    sell = 0
    cnt.sort(reverse=True)
    for i in cnt:
        sell += i
        if sell >= k:
            return box + 1
        else:
            box += 1