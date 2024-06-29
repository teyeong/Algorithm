def cut_paper(paper):
    white = 0
    blue = 0
    if len(paper) == 1: # 더이상 나눌 수 없을 때
        if paper[0][0] == 0:
            white += 1
        else:
            blue += 1
        return white, blue
    
    color = -1
    flag = 0
    length = len(paper[0])
    
    for i in range(len(paper)):
        if sum(paper[i]) == 0:
            if i == 0:
                color = 0
            elif color != 0:
                flag = 1
        elif sum(paper[i]) == len(paper[i]):
            if i == 0:
                color = 1
            elif color != 1:
                flag = 1
        else:
            flag = 1

        if flag == 1:
            break
    
    if flag:
        left_up = list(paper[i][: length // 2] for i in range(length // 2))
        left_down = list(paper[i][: length // 2] for i in range(length // 2, length))
        right_up = list(paper[i][length // 2 :] for i in range(length // 2))
        right_down = list(paper[i][length // 2 :] for i in range(length // 2, length))
        w1, b1 = cut_paper(left_up)
        w2, b2 = cut_paper(left_down)
        w3, b3 = cut_paper(right_up)
        w4, b4 = cut_paper(right_down)
        white += w1 + w2 + w3 + w4
        blue += b1 + b2 + b3 + b4
    else:
        if color == 1:
            blue += 1
        elif color == 0:
            white += 1
    return white, blue

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = cut_paper(paper)
print(white, blue, sep="\n")