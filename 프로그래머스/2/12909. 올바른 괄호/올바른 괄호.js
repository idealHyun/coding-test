function solution(s){
    let a=0;

    for(let i=0;i<s.length;i++){
        if(s[i]==='('){
            a++;
        }
        else{
            a--;
            if(a<0)
                break;
        }
    }

    return a===0 ? true : false;
}