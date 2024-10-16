def convert_to_binary(num, n):
    # bin() 함수를 이용해 이진수 변환 후 앞의 '0b' 제거하고 zfill로 자리수 맞춤
    return bin(num)[2:].zfill(n)

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        string1 = convert_to_binary(arr1[i], n)
        string2 = convert_to_binary(arr2[i], n)
        
        line = [
            "#" if string1[j] == "1" or string2[j] == "1" else " " 
            for j in range(n)
        ]
        
        answer.append("".join(line))
        
    return answer