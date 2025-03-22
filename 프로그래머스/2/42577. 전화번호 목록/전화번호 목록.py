def solution(phone_book):
    # 길이순 정렬
    phone_book.sort()
    
    for idx, val in enumerate(phone_book[:len(phone_book) - 1]):
        if phone_book[idx + 1].startswith(val):
            return False
    
    return True