import collections

def solution(nums):
    answer = 0
    counter = collections.Counter(nums)
    if len(nums) // 2 < len(counter):
        answer = len(nums) // 2
    else:
        answer = len(counter)
    
    
    return answer