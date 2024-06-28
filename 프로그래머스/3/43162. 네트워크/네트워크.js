function solution(n, computers) {
    var answer = 0;
    let visited=new Array(n).fill(false);
    
    function dfs(k){
        visited[k]=true;
        for(let j=0;j<n;j++){
            if(!visited[j] && computers[k][j]===1){
                dfs(j);
            }
                
        }
    }
    
    for(let i=0;i<n;i++){
        if(!visited[i]){
            answer++;
            dfs(i);
        }
    }
    
    return answer;
}