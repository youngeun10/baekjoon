def solution(phone_book):

    phone_book.sort()

    for i in range(len(phone_book)-1):
        std = phone_book[i]
        if phone_book[i+1].startswith(std):
            return False
    return True