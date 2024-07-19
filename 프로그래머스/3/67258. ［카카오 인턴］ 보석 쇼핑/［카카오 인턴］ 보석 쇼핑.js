function solution(gems) {
    let answer=[];
    let gemNum=new Set(gems).size;
    let start=0;
    let gemMap=new Map();
    let distance=gems.length+2; // 시작점과 끝점 거리
    
    for(let i=0;i<gems.length;i++){
        // 보석 개수 구하기
        if(gemMap.get(gems[i])!=undefined)
            gemMap.set(gems[i],gemMap.get(gems[i])+1);
        else
            gemMap.set(gems[i],1);
        
        // 보석 개수 맞으면 최소 거리 구하기
        while(gemMap.size===gemNum){
            // 시작점의 보석의 개수가 2개 이상일때는 제거
            if(gemMap.get(gems[start])>1){
                gemMap.set(gems[start],gemMap.get(gems[start])-1)
                start++;
                if(i-start<distance){
                    answer=[start+1,i+1];
                    distance=i-start;
                }
            }
            // 시작점의 보석의 개수가 1개이므로 distance 확인
            else{
                if(i-start<distance){
                    answer=[start+1,i+1];
                    distance=i-start;
                }
                break;
            }
        }
    }
    
    return answer;
}