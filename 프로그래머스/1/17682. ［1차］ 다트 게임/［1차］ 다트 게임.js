function solution(dartResult) {
    var answer = 0;
    const scoreArray = [];
    let index = -1;
    let number = '';
    
    for(let i=0;i<dartResult.length;i++){
        switch(dartResult[i]){
            case 'S':
                scoreArray.push(number);
                number='';
                index++;
                break;
            case 'D':
                scoreArray.push(Math.pow(number,2));
                number='';
                index++;
                break;
            case 'T':
                scoreArray.push(Math.pow(number,3));
                number='';
                index++;
                break;
            // *이 나오면 전 점수와 전전 점수를 2배
            case '*':
                scoreArray[index] *= 2;
                if(index>=1){
                    scoreArray[index-1] *= 2;
                }
                break;
            // #이 나오면 전 점수를 마이너스를 곱해주기 
            case '#':
                scoreArray[index] *= -1;
                break;
            // 숫자
            default :
                number+=dartResult[i];
                number = Number(number);
        }
    }
    scoreArray.forEach((score)=>answer+=score)
    return answer;
}