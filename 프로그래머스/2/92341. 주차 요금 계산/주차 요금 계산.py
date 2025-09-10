import heapq
import math

def solution(fees, records):
    answer = []
    
    cars = dict()
    
    for record in records:
        r = list(record.split())
        if r[1] not in cars.keys():
            cars[r[1]] = []

        cars[r[1]] += [(r[0], r[2])]
        
    for car in cars:
        price = 0 # 요금 합계
        curr_state = '' # 현재 상태
        curr_time = 0 # 누적 주차 시간
        in_h, in_m, out_h, out_m = 0, 0, 0, 0
        
        for i in cars[car]:          
            if i[1] == 'IN': # IN일 때
                in_h, in_m = map(int, i[0].split(':'))
                curr_state = 'IN'
            else: # OUT일 때
                out_h, out_m = map(int, i[0].split(':'))
                curr_state = 'OUT'
                
                # 시간 계산
                h = out_h - in_h
                m = out_m - in_m
                curr_time += h * 60 + m
                
        if curr_state == 'IN': # 출차된 내역이 없는 경우
            h = 23 - in_h
            m = 59 - in_m
            curr_time += h * 60 + m
        
        if curr_time > fees[0]:
            price += math.ceil((curr_time - fees[0]) / fees[2]) * fees[3] # 초과 요금
        price += fees[1] # 기본 요금
        
        # cars 딕셔너리 업데이트
        cars[car] = price
    
    # 딕셔너리 정렬
    tup = sorted(cars.items(), key=lambda x: x[0])
    answer = [val[1] for val in tup]
    
    return answer