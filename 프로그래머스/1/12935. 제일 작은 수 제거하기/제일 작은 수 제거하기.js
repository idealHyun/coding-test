function solution(arr) {
    var answer = [];
    if(arr.length==1){
        return [-1];
    }
    minNum =Math.min(...arr)
    arr = arr.filter(x=> x!==minNum)
    
    return arr;
}