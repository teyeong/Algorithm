def count_test_proctor(n, a, b, c):
    cnt = 0
    for i in range(n):
        if (b >= a[i]):                 # 총감독관만 할당
            cnt += 1
        else:
            a[i] -= b                   # 총감독관 할당
            cnt += 1
            
            cnt += (a[i] // c)          # 부감독관 할당
            if a[i] % c > 0:
                cnt += 1
    return cnt
    
n = int(input())                        # 시험장의 개수 N

a = list(map(int, input().split()))     # 각 시험장에 있는 응시자 수 Ai

b, c = map(int, input().split())        # 총감독관이 감시 가능한 인원 B, 부감독관이 감시 가능한 인원 C

cnt = count_test_proctor(n, a, b, c)
print(cnt)