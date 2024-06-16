def count(X, Y):
    cnt = 0
    for i in range(len(X)):
        if X[i] == Y[i]:
            cnt += 1
    return cnt

def check(X, Y):
    while len(X) != len(Y):
        max_cnt = -1
        idx = -1
        for j in range(len(Y) - len(X) + 1):
            temp_cnt = count(X, Y[j:j+len(X)])
            if temp_cnt > max_cnt:
                max_cnt = temp_cnt
                idx = j
        if idx == 0:
            X.append(Y[idx + len(X)])
        else:
            X.insert(0, Y[idx - 1])

    return len(X) - count(X, Y)

X, Y = input().split()

X = list(X)
Y = list(Y)

print(check(X, Y))