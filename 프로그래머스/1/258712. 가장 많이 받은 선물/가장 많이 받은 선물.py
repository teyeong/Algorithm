def solution(friends, gifts):
    idx = {}
    length = len(friends)
    for i in range(length):
        idx[friends[i]] = i
    
    arr = [[0 for _ in range(length)] for _ in range(length)]
    ans = [0] * length

    for ch in gifts:
        fr, to = map(str, ch.split())
        arr[idx[fr]][idx[to]] += 1
    
    for i in range(length - 1):
        for j in range(i + 1, length):
            a = arr[idx[friends[i]]][idx[friends[j]]]
            b = arr[idx[friends[j]]][idx[friends[i]]]
            if a > b:
                ans[idx[friends[i]]] += 1
            elif a < b:
                ans[idx[friends[j]]] += 1
            else:
                a_num = sum(arr[idx[friends[i]]]) - sum(row[idx[friends[i]]] for row in arr)
                b_num = sum(arr[idx[friends[j]]]) - sum(row[idx[friends[j]]] for row in arr)
                if a_num > b_num:
                    ans[idx[friends[i]]] += 1
                elif a_num < b_num:
                    ans[idx[friends[j]]] += 1
    return max(ans)