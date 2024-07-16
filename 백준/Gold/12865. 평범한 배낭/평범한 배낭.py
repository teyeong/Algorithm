N, K = map(int, input().split())

items = [[0, 0]]
# N번째 물건까지 보았을 때 무게가 K인 배낭의 최대 가치
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    items.append(list(map(int, input().split())))
    
for i in range(1, N + 1):
    for j in range(1, K + 1): # 배낭 허용 무게 j
        W = items[i][0]
        V = items[i][1]
        
        if j < W:
            dp[i][j] = dp[i - 1][j]
        else:
            # 1. 현재 물건을 넣지 않고 이전 배낭 그대로
            # 2. W만큼 배낭에서 빼고 V(현재 물건) 넣기: 가방에 새거 넣기
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)

print(dp[N][K])