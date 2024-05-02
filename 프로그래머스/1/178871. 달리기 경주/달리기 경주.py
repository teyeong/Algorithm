def solution(players, callings):
    
    play_dict = dict({player: i for i, player in enumerate(players)})
    
    for i in callings:
        index = play_dict[i]
        play_dict[i] -= 1
        play_dict[players[index - 1]] += 1
        players[index - 1], players[index] = players[index], players[index - 1]
    
    return players