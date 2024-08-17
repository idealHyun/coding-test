function solution(s) {
    var answer = '';
    const array=s.split(' ');
    for(let i=0;i<array.length;i++){
        if(array[i].length>0){
            // 숫자가 아닌 경우
       if(isNaN(parseInt(array[i][0]))){
           array[i] = array[i][0].toUpperCase() + array[i].slice(1).toLowerCase();
       }
        else{
            array[i] = array[i][0] + array[i].slice(1).toLowerCase();
        }
        }
        
    }
    answer = array.join(' ');
    return answer;
}