function solution(ingredient) {
    var answer = 0;
    var stack = [];
    
    for(let i = 0; i < ingredient.length; i++) {
        stack.push(ingredient[i]);
        
        // 스택의 마지막 4개의 요소가 "1231"인지 확인
        if (stack.length >= 4 && stack.slice(-4).join('') === '1231') {
            // "1231"을 제거
            stack.splice(-4);
            answer++;
        }
    }
    
    return answer;
}