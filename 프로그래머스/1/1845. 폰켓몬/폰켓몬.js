function solution(nums) {
    var answer = 0;
    const ponketmonMap=nums.reduce((acc,ponketmon)=>{
        if(acc[ponketmon]===undefined)
            acc[ponketmon]=0;
        else 
            acc[ponketmon]++;
        return acc;
    },{})
    for(let ponketmon in ponketmonMap){
        answer++;
        if(answer>=nums.length/2)
            break;
    }
    
    return answer;
}