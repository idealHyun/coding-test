function solution(s){
    var answer = true;
    var pCount=0, yCount=0;
    
    for(let i=0;i<s.length;i++){
        console.log(s[i])
        if(s[i] ==='y' || s[i] ==='Y')
            yCount++;
        else if(s[i] ==='p' || s[i] ==='P')
            pCount++;
    }
    
    if(pCount != yCount)
        answer=false;

    return answer;
}