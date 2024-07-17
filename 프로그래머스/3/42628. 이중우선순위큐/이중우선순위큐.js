function solution(operations) {
    var answer = [];
    
    for (let i = 0; i < operations.length; i++) {
        const [first, second] = operations[i].split(' ');
        
        if (first === "I") {
            answer.push(Number(second));
        } else if (first === "D" && second === "1") {
            // 최대값 삭제
            if (answer.length > 0) {
                const max = Math.max(...answer);
                const maxIndex = answer.indexOf(max);
                answer.splice(maxIndex, 1);
            }
        } else if (first === "D" && second === "-1") {
            // 최소값 삭제
            if (answer.length > 0) {
                const min = Math.min(...answer);
                const minIndex = answer.indexOf(min);
                answer.splice(minIndex, 1);
            }
        }
    }
    
    if (answer.length === 0) {
        return [0, 0];
    } else {
        const max = Math.max(...answer);
        const min = Math.min(...answer);
        return [max, min];
    }
}