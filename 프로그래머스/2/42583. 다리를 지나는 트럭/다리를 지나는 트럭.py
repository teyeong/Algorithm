def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge = [0 for _ in range(bridge_length)]
    total = 0
    
    while truck_weights or total > 0:
        answer += 1
        total -= bridge.pop(0)
        if truck_weights and truck_weights[0] + total <= weight:
            curr = truck_weights.pop(0)
            bridge.append(curr)
            total += curr
        else:
            bridge.append(0)
    
    return answer