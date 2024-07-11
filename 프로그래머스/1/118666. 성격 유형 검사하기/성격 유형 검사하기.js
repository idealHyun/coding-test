function solution(survey, choices) {
    var answer = '';
    let acc={};
    
    // 초기화
    let keys = ['R','T', 'C', 'F', 'J', 'M', 'A', 'N'];

    for (let key of keys) {
        acc[key] = 0;
    }
    
    // 점수 계산
    const scores = [3, 2, 1, 0, 1, 2, 3];

    for (let i = 0; i < survey.length; i++) {
        let [disagree, agree] = survey[i].split('');
        let choice = choices[i];
        
        if (choice <= 3) {
            acc[disagree] += scores[choice - 1];
        } else if (choice >= 5) { 
            acc[agree] += scores[choice - 1];
        }
    }
    
    // 계산한 결과로 결과 도출
    for(let j=0;j<keys.length;j+=2){
        if(acc[keys[j]]>=acc[keys[j+1]])
            answer+=keys[j];
        else 
            answer+=keys[j+1];
    }
    
    return answer;
}