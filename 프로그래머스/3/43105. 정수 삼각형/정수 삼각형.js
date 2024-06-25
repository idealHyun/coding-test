function solution(triangle) {
    var answer = 0;
    let T=Array.from(Array(triangle.length), () => []);
    T[0][0]=triangle[0][0];
    
    for(let i=1;i<triangle.length;i++){
        for(let j=0;j<i+1;j++){
            let node=triangle[i][j];
            let p1;
            let p2;
            T[i-1][j]===undefined ? p1=0 : p1=T[i-1][j];
            T[i-1][j-1]===undefined ? p2=0 : p2=T[i-1][j-1];
            
            if(node+p1>node+p2)
                T[i][j]=node+p1;
            else
                T[i][j]=node+p2;
        }
    }
    answer=Math.max(...T[triangle.length-1])
    return answer;
}