import sys
input = sys.stdin.readline

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

win = 0 # 슬라이딩 윈도우
max_visitors = 0 # 방문자 수 최대값
visit_dict = dict()

win = sum(visitors[:X])
max_visitors = max(max_visitors, win)
visit_dict[win] = 1

for idx in range(X, N):
    win += visitors[idx] - visitors[idx - X]
    max_visitors = max(max_visitors, win)
    if win in visit_dict.keys():
        visit_dict[win] += 1
    else:
        visit_dict[win] = 1

# 정답 출력
if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(visit_dict[max_visitors])