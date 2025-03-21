import heapq

def solution(operations):
    answer = []
    heap = []
    
    for op in operations:
        if 'I' in op:
            _, num = op.split()
            heapq.heappush(heap, int(num))
        elif heap:
            if 'D 1' == op:
                before = []
                after = []
                for n in heap:
                    heapq.heappush(before, -n)
                heapq.heappop(before)
                for n in before:
                    heapq.heappush(after, -n)
                heap = after
            elif 'D -1' == op:
                heapq.heappop(heap)
    return [max(heap), min(heap)] if heap else [0, 0]