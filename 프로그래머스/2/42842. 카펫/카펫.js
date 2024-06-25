function solution(brown, yellow) {
    var answer = [];
    let total=brown+yellow;
    for(let i=3; i<=Math.sqrt(total);i++){
        if(total%i==0 && (total/i+i-2)*2==brown)
            answer=[total/i,i];
    }
    return answer;
}