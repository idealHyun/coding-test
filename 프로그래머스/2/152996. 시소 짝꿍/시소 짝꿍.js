function solution(weights) {
    var answer = 0;
    
    // 객체에 각 해당 값의 개수를 파악
    var weightCount=weights.reduce((acc,weight)=>{
        if(acc[weight]){
            acc[weight]++;
        }
        else {
            acc[weight]=1;
        }
        return acc;
        
    },{})
    
    // 객체의 키를 배열로 변환
    var keys = Object.keys(weightCount).map(Number);
    
    // 2차원 반복문을 통해 비교
    for (let i = 0; i < keys.length; i++) {
        let weight1 = keys[i];
        if(weightCount[weight1]>1){
            answer+= (weightCount[weight1]*(weightCount[weight1]-1))/2
        }
        
        for (let j = i+1; j < keys.length; j++) {
            let weight2 = keys[j];
            
            if(weight1*2===weight2 || weight1===weight2*2 || weight1*3===weight2*2 ||weight1*2 ===weight2*3 ||weight1*3===weight2*4 ||weight1*4===weight2*3 ){
                
                answer+= weightCount[weight1] * weightCount[weight2];
            }
        }
    }
    
    
    
    
    return answer;
}