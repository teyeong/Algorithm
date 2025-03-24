def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    max_x = max(sizes[i][0] for i in range(len(sizes)))
    max_y = max(sizes[i][1] for i in range(len(sizes)))
    return max_x * max_y