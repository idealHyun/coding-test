function solution(numbers) {
    var answer = [];
    answer[numbers.length-1]=-1;
    for(let i=numbers.length-2;i>=0;i--){
        for(let j=i+1;j<numbers.length;j++){
            if(numbers[i]<numbers[j]){
                answer[i]=numbers[j];
                break;
            }
            else {
                if(numbers[i]<answer[j]){
                    answer[i]=answer[j];
                    break;
                } else if(answer[j]===-1){
                    answer[i]=-1;
                    break;
                }
            }
        }
    }
    
    return answer;
}