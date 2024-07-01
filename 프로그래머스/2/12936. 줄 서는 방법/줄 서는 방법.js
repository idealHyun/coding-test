function factorial(n) {
    let result = 1;
    for (let i = 1; i <= n; i++) {
        result *= i;
    }
    return result;
}

function solution(n, k) {
    var answer = [];
    const people = Array.from({ length: n }, (_, i) => i + 1);
    for(let i=n;i>=1;i--){
        let x=factorial(i-1);
        for(let j=0;j<i;j++){
            if(k>x*(j+1))
                continue;
            else{
                k=k-x*j;
                answer.push(people[j])
                people.splice(j,1);
                break;
            }
        }
    }
    return answer;
}