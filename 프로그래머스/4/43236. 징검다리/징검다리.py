def solution(distance, rocks, n):
    answer = 0
    
    # 정렬
    rocks.sort()
    
    left = 1
    right = distance
    
    while left <= right:
        mid = (left + right) // 2
        cnt = 0 # 제거한 바위 개수 카운트 변수
        curr = 0 # 현재 위치
        for i in range(len(rocks)):
            if rocks[i] - curr < mid: # 중간값보다 거리가 작은 경우엔 제거
                cnt += 1
            else:
                curr = rocks[i]
        
        if distance - curr < mid:
            # 가장 오른쪽에 있는 경우
            cnt += 1
        
        if cnt <= n:
            answer = mid
            # mid 값 키우기
            left = mid + 1
        elif cnt > n:
            # mid 값 줄이기
            right = mid - 1
        
    return answer