def solution(phone_book):
    answer = True
    hashMap = {}

    for number in phone_book:
        hashMap[number]='';
        
    length = len(phone_book)
                 
    for number in phone_book:
        for i in range(len(number)):
            if number[:i] in hashMap:
                return False
            
    return answer