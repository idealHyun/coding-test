function solution(s) {
    let transCount=0;
    let zeroCount=0;
    
    while(s !== '1'){
        transCount++;
        let oneCount=0;
        let sLength=s.length;
        
        for(let i=0;i<sLength;i++){
            if(s[i]== 1){
                oneCount++;
            }
        }
        
        zeroCount += (sLength - oneCount);
        
        let string = '';
        
        while(Math.floor(oneCount / 2) >= 1){
            if(oneCount % 2 === 1)
                string += '1'
            else
                string += '0'
            oneCount = Math.floor(oneCount/2);
        }
        
        string += '1';
        string.split('').reverse().join('');
        s=string;
    }
    
    return [transCount,zeroCount];
}