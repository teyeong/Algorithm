def solution(prices):
    answer = [0 for _ in range(len(prices))]
    
    for idx, price in enumerate(prices):
        for j in range(idx + 1, len(prices)):
            answer[idx] += 1
            if prices[j] < price:
                break
    
    return answer