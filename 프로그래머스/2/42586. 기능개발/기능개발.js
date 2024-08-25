function solution(progresses, speeds) {
    var answer = [];
    while(progresses.length>0){
        let count=0; // 해당 일에 배포가능한 작업 수
        
        // 모든 진행률 돌면서 해당 속도를 더하기
        for(let i=0;i<progresses.length;i++){
            progresses[i]+=speeds[i];
            if(progresses[i]>=100)
                progresses[i]=100;
        }
        
        // 100인 진행률이 있으면 앞에서부터 뒤에까지 개수세서 answer에 넣기
        for(let i=0;i<progresses.length;i++){
            if(progresses[i]===100)
                count++;
            else
                break;
        }
        
        // 진행률 100인 개수 배열에서 제거
        if(count!==0){
            progresses.splice(0,count);
            speeds.splice(0,count);
            answer.push(count)
        } 
    }
    return answer;
}