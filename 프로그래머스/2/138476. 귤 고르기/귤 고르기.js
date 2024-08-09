function solution(k, tangerine) {
    var answer = 0;
    const tangerineMap= tangerine.reduce((acc,tang)=>{
        if(acc[tang]=== undefined){
            acc[tang]=1;
        }    
        else {
            acc[tang]++;
        }
        return acc;
    },{})
    
    // 객체의 내용물을 내림차순으로 정렬
    const sortedTangerineArray = Object.entries(tangerineMap).sort((a, b) => b[1] - a[1]);

    let count = 0;
    for (let [tang, quantity] of sortedTangerineArray) {
        answer++;
        count += quantity;
        if (count >= k) return answer;
    }

    return answer;
}