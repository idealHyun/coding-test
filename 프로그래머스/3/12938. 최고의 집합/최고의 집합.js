function solution(n, s) {
    var answer = [];
    
    if(n===1)
        answer.push(s);
    else if(s/n<1)
        answer.push(-1);
    else {
        if(s%n===0){
            for(let i=0;i<n;i++)
                answer.push(s/n);
        }
        else{
            for(let i=0;i<n-s%n;i++)
                answer.push(Math.floor(s/n));
            for(let i=0;i<s%n;i++)
                answer.push(Math.floor(s/n)+1);
        }
    }
    
    return answer;
}