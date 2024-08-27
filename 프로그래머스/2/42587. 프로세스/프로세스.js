function solution(priorities, location) {
    var answer = 0;
    // 큐에 넣기
    let queue = [];
    for(let i=0;i<priorities.length;i++){
        queue.push(i);
    }
    // map 만들기
    let map = priorities.reduce((acc,value,index)=>{
        acc[index]=priorities[index];
        return acc;
    },{})
    // 큐에서 꺼내서 확인
    while(queue.length>0){
        let process=queue[0]; // index 값
        let processCount=1; // 큐 맨뒤로 보낼 프로세스 개수
        let count=0;
        console.log("맵확인",map)
        console.log("큐확인",queue)
        // 우선순위 비교
        for(let i=0;i<queue.length;i++){
            count++;
            if(map[process]<map[queue[i]]){
                processCount=count;
                process=queue[i]
            }   
        }
        // 우선순위로 큐에 내용 제거
        answer++;
        let restProcess=queue.splice(0,processCount);
        queue.push(...restProcess.splice(0,processCount-1));
        delete map[process];
        if(location==process)
            break;
    }
    return answer;
}