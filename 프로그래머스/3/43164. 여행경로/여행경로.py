def solution(tickets):
    airport = {}
    
    for val in tickets:
        if val[0] in airport.keys():
            airport[val[0]] += [(val[1], False)]
        else:
            airport[val[0]] = [(val[1], False)]
    
    for key in airport:
        airport[key].sort()
        
    path = []
    length = len(tickets) + 1
    
    def dfs(start, cnt):
        path.append(start)

        if cnt == length:
            return True

        if start in airport:
            for idx, (dest, used) in enumerate(airport[start]):
                if not used:
                    airport[start][idx] = (dest, True)
                    if dfs(dest, cnt + 1):
                        return True
                    airport[start][idx] = (dest, False)  # 백트래킹
        path.pop()
        return False
    
    dfs("ICN", 1)
    
    return path