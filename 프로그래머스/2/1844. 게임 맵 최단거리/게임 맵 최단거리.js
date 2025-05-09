function solution(maps) {
    var answer = 0;
    const n=maps.length;
    const m=maps[0].length;
    
    // 상, 우, 하, 좌
    const dx=[0,1,0,-1];
    const dy=[1,0,-1,0];
    const visited=Array.from({length:n},()=>Array(m).fill(false));
    
    function bfs(){
        const q=[];
        q.push([0,0,0]);
        visited[0][0]=true;
        while (q.length!==0){
            [y,x,count] = q.shift();
            
            if(y===n-1 && x===m-1){
                answer = count+1
                return
            }
            
            for(let i=0;i<4;i++){
                const ny = y+dy[i]
                const nx = x+dx[i]
                if ( ny < n && ny >=0 && nx < m && nx >=0 && maps[ny][nx]!==0 && visited[ny][nx]==false){
                    visited[ny][nx]=true
                    q.push([ny,nx,count+1])
                }
            }
        }
    }
    
    bfs();
    
    if(answer==0){
        return -1
    }
    return answer;
}