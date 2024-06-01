def solution(n,a,b):
    answer = 1

    while n > answer:
        if abs(a - b) == 1 and min(a, b) % 2 == 1:
            break
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2

    return answer