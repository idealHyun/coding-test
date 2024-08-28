function solution(n) {
    var arr = [0, 1]; // 초기값 F(0), F(1) 지정
    // 미리 계산
    for (var i = 2; i <= n; i++) {
        arr[i] = (arr[i - 1] + arr[i - 2]) % 1234567;
    }
    
    return arr[n];
}