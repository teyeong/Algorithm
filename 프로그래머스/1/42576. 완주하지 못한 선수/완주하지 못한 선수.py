import collections
def solution(participant, completion):
    counter = collections.Counter(participant)
    for name in completion:
        counter[name] -= 1
    for name, cnt in counter.items():
        if cnt > 0:
            return name
    return