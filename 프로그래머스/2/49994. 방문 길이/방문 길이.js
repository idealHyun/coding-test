function solution(dirs) {
    let x=0;
    let y=0;
    let dirsSet= new Set();
    for(let i=0;i<dirs.length;i++){
        
        switch(dirs[i]){
            case 'U':{
                if(y<5){
                    dirsSet.add(`${x}${y}${x}${y+1}`);
                    y+=1;
                }
                break;
            }
            case 'L':{
                if(x>-5){
                    dirsSet.add(`${x-1}${y}${x}${y}`);
                    x-=1;   
                }
                break;
            }
            case 'R':{
                if(x<5){
                    dirsSet.add(`${x}${y}${x+1}${y}`);
                    x+=1;
                }
                break;
            }
            case 'D':{
                if(y>-5){
                   dirsSet.add(`${x}${y-1}${x}${y}`);
                    y-=1; 
                }
                break;
            }
        }
    }
    
    
    return dirsSet.size;
}