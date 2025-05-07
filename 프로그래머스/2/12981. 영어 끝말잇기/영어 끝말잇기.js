function solution(n, words) {
    let answer = [];
    let wordSet = new Set();
    let count = 0;
    let isFail = false;
    let lastChar = null;
    
    for(const word of words){
        if(lastChar !== null){
            if(wordSet.has(word) || lastChar !== word[0]){
            isFail=true;
            break;
            }
        }
        
        wordSet.add(word);
        lastChar = word.at(-1);
        count += 1;
    }
    
    if(isFail){
        answer.push(count % n +1);
        answer.push(Math.floor(count/n) +1);
    } else{
        return [0,0];
    }
    

    return answer;
}