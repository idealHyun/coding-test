def solution(s):
    arr = [int(x) for x in s.split(" ")]
    arr.sort();
    min = arr[0];
    max = arr.pop();
    return f"{min} {max}"