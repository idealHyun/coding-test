function solution(participant, completion) {
    var answer = '';
    const a= participant.reduce((acc,person)=>{
        if(acc[person]===undefined){
            acc[person]=1;
        } else{
            acc[person]++;
        }
        return acc;
    },{})
    const b= completion.reduce((acc,person)=>{
        if(acc[person]===undefined){
            acc[person]=1;
        } else{
            acc[person]++;
        }
        return acc;
    },{})
    for(let name in a){
        if(a[name]!=b[name])
            return name;   
    }
    return answer;
}