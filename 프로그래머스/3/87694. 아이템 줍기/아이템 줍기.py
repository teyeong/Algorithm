from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    terrain = [[0 for _ in range(101)] for _ in range(101)]
    
    limit = 0 # 지형 한계값
    # 직사각형 채우기
    for idx, rec in enumerate(rectangle):
        limit = max(limit, max(rec) * 2)
        for x in range(rec[1] * 2, rec[3] * 2 + 1):
            for y in range(rec[0] * 2, rec[2] * 2 + 1):
                terrain[x][y] = 1
    
    # 내부 삭제
    for rec in rectangle:
        for x in range(rec[1] * 2 + 1, rec[3] * 2):
            for y in range(rec[0] * 2 + 1, rec[2] * 2):
                terrain[x][y] = 0
    
    visit = [[False for _ in range(limit + 1)] for _ in range(limit + 1)]
    queue = deque()
    
    # 시작 초기화
    queue.append((characterY * 2, characterX * 2, 0))
    visit[characterY * 2][characterX * 2] = True
    
    while queue:
        x, y, cnt = queue.popleft()
        
        # 종료 시점
        if x == itemY * 2 and y == itemX * 2:
            answer = cnt // 2
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx <= limit and 0 <= ny <= limit:
                if terrain[nx][ny] == 1 and visit[nx][ny] == False:
                    queue.append((nx, ny, cnt + 1))
                    visit[nx][ny] = True
                    
    return answer