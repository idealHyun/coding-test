def solution(word):
    alphabet = ["A", "E", "I", "O", "U"]
    answer = 0

    def backtracking(tmp, w):
        nonlocal answer
        if "".join(tmp) == w:
            return True
        
        for a in alphabet:
            if len(tmp) < 5: 
                tmp.append(a)
                answer += 1 
                if backtracking(tmp, w):
                    return True
                tmp.pop()

        return False

    backtracking([], word)
    return answer
