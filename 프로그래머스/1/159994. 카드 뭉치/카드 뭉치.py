def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    index1 = 0
    index2 = 0
    
    for i in range(len(goal)):
        if index1 < len(cards1) and goal[i] == cards1[index1]:
            index1 += 1
        elif index2 < len(cards2) and goal[i] == cards2[index2]:
            index2 += 1
            print(cards2)
        else:
            answer = 'No'
            break
    
    return answer