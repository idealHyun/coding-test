function solution(n, works) {
    var answer = 0;
    // 작업량이 n보다 작으면 0 반환
    if (works.reduce((a, b) => a + b, 0) <= n) {
        return 0;
    }
    
    // works 내림차순 정렬
    works.sort((a,b)=>b-a);
    
    while (n > 0) {
        // 가장 큰 작업량을 1 줄임
        works[0] -= 1;
        n--;

        // 다시 정렬하여 최대값이 맨 앞에 오도록 함
        for (let i = 0; i < works.length - 1; i++) {
            if (works[i] < works[i + 1]) {
                [works[i], works[i + 1]] = [works[i + 1], works[i]];
            } else {
                break;
            }
        }
    }
    
    // 야근지수 계산
    return works.reduce((a, b) => a + b * b, 0);
}