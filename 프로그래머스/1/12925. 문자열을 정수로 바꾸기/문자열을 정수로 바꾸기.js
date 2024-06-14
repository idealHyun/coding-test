function solution(s) {
    var answer = 0;
    
    switch(s[0]){
        case '+':{
            answer=Number(s.substring(1));
            break;
        }
            case '-':{
            answer=Number(s.substring(1))*-1;
            break;
        }
            default:{
            answer=Number(s)
            break;
        }
    }
    
    return answer;
}